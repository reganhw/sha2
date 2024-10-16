import grp512.sigma512 as sigma512
from bitwise_funcs import*
from grp512.constants import *

def str_to_bin(M):
    '''
    Takes in a string M and converts it to a binary string.
    '''
    Mbytes = M.encode()
    return ''.join(format(x,'08b') for x in Mbytes)

def get_hash(s0,s1,S0,S1, get_k, M, form="hex",):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    mbl = 1024    # message block length
    # --------------------------------------- Preprocessing ----------------------------------------

    def padding(M):
        '''
        Takes in a string M, converts to a binary string of length l and appends:
        - One "1"
        - k zeros such that 1+l+k := 896 mod 1024
        - l in 64 bits
        '''
        Mb= str_to_bin(M)
        l = len(Mb)                        # l = message length
        k = get_k(l)                       # calculate k
        zeros = "0"*k                      # k zeros
        lb = format(l, '0128b')            # l in 128bits
        return Mb + "1"+zeros+lb

    # ---------------------------------Page 14, section 5.2.1.---------------------------------

    def str_to_blocks(M):
        '''
        Input: String of length 1024n for some n.
        Output: String array, M split into blocks of length bl.
        '''
        if(len(M)&(mbl-1)!=0):
           raise ValueError("Input string must have length bl*n for some n.")

        total_blocks = int(len(M)/mbl)    # number of total blocks
        message_blocks = []               # array to store values
        for i in range (total_blocks):
            block = M[mbl*i:mbl*(i+1)]
            message_blocks.append(block)
        return message_blocks

    def split_64bit(M):
        '''
        Input: String M of length 1024.
        Output: Integer array, M split into 16 blocks of 64 bits, each block then converted to an integer.
        '''
        if(len(M)!=1024):
            raise ValueError('M must have length 1024.')
        output = []
        for i in range (16):
            block = M[64*i:64*(i+1)]
            output.append(int(block,2))
        return output    

    # --------------------------------------- Hashing ----------------------------------------
    M_padded = padding(M)                                  # pad M.
    M_blocks = str_to_blocks(M_padded)                       # split into 1024 bit blocks.
    H = initial_hash_512.copy()
    def message_schedule(M):
        '''
        Input: String M of length 1024.
        Output: Array of 80 integers, message schedule as described in the NIST document
        '''
        W = split_64bit(M).copy()
        for t in range(16,80):
            Wt = (s1(W[t-2]) + W[t-7] + s0(W[t-15])+W[t-16])&MASK
            W.append(Wt)
        return W
    
    def my_update_variables(W):
        a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
        for t in range (80):
            T1 = (h + S1(e) + Ch(e,f,g, MASK) +K512[t] + W[t])&MASK
            T2 = (S0(a) + Maj(a,b,c))&MASK
            h = g
            g = f
            f = e
            e = (d + T1)&MASK
            d = c
            c=b
            b=a
            a = (T1 + T2)&MASK
        return a,b,c,d,e,f,g,h
                                                             # intialise hash.
    for block in M_blocks:                                   # for each message block...
        W = message_schedule(block)                          # obtain message schedule.
        working_variables = my_update_variables(W)           # obtain working variables.
        for j in range (8):                                  
            H[j] = (H[j]+ working_variables[j])&MASK         # update hash values (section 6.2.2-4.)
    
    if(form=="bin"):
        return ''.join(format(h, '064b') for h in H) # convert final hash values into binary string.
    
    return ''.join(format(h, '016x') for h in H) # convert final hash values into hex string.

def sha512(M):
    s0 = sigma512.sig0
    s1 = sigma512.sig1
    S0 = sigma512.Sig0
    S1 = sigma512.Sig1
    def get_k(l):
        '''
        Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 896 mod 1024.
        '''
        n = (l+1)&1023           # & 1023 is equivalent to %1024
        return (896-n)&1023
    return get_hash(s0 = s0, s1 = s1, S0=S0, S1 = S1, get_k = get_k, M=M)

if __name__=='__main__':
    import hashlib
    s = ""
    for i in range(5):
        # Check hex version.
        hash_hex = sha512(s)
        verified_func = getattr(hashlib, "sha512")  # hashlib.sha
        verified_hash_hex = verified_func(s.encode()).hexdigest()

        # Check bin version.
        '''
        bin_length = len(hash_hex)*4
        hash_bin =sha512(s,'bin')
        verified_hash_bin = format(int(verified_hash_hex,16), f'0{bin_length}b')
        assert(hash_bin==verified_hash_bin)
        '''
        # Update s to be: (current string) + (its hash) + (a special chr).
        s = s + hash_hex

    print(sha512("helloworld"))
