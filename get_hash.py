from basic_funcs import *

def get_hash(config, M, form="hex",):
    '''
    Input: Message string M of any length.
    Output: The hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    MASK = config['MASK']
    bl = config['bl']         # bit length: values are regarded as a bl-bit integer
    mbl = config['mbl']       # message block length
    t_lim = config['t_lim']   # upper limit for 't' in main hashing part

    K = config['K_constants']
    H = config['initial_hash'].copy() 

    s0 = config['s0']
    s1 = config['s1']
    S0 = config['S0']
    S1 = config['S1']

    get_k = config['get_k']

    # --------------------------------------- Preprocessing ----------------------------------------

    def padding(M):
        '''
        Takes in a string M, converts to a binary string of length l and appends:
        - One "1"
        - k zeros, defined by get_k
        - l encoded in binary
        '''
        Mb= str_to_bin(M)
        l = len(Mb)                        # l = message length
        k = get_k(l)                       # calculate k
        zeros = "0"*k                      # k zeros
        lb = format(l, f'0{bl*2}b')        # l in 64 or 128bits
        return Mb + "1"+zeros+lb

    def str_to_blocks(s):
        '''
        Input: String of length (message block length)n for some n.
        Output: String array, s split into blocks of length bl.
        '''
        if(len(s)&(mbl-1)!=0):
           raise ValueError("Input string must have length mbl*n for some n.")

        block_num = int(len(s)/mbl)    # number of total blocks
        message_blocks = [s[mbl*i:mbl*(i+1)] for i in range(block_num)]               
        return message_blocks

    def get_word_blocks(s):
        '''
        Input: String s which is a message block.
        Output: Integer array. The message block is split into 16 blocks of bl bits.
        Then, each block then converted to an integer.
        '''
        if(len(s)!=mbl):
            raise ValueError(f'Input string must have length {mbl}.')
        
        word_blocks = []
        for i in range (16):
            block = s[bl*i:bl*(i+1)]
            word_blocks.append(int(block,2))
            
        return word_blocks    

    # --------------------------------------- Hashing ----------------------------------------

    def message_schedule(s):
        '''
        Input: String s which is a message block.
        Output: List of integers, which is the message schedule as described in the NIST document.
        '''
        W = get_word_blocks(s).copy()
        for t in range(16,t_lim):
            Wt = (s1(W[t-2]) + W[t-7] + s0(W[t-15])+W[t-16])&MASK
            W.append(Wt)
        return W
    
    def my_update_variables(W):
        a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
        for t in range (t_lim):
            T1 = (h + S1(e) + Ch(e,f,g, MASK) +K[t] + W[t])&MASK
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
    
    def main():
        M_padded = padding(M)                                    # pad M.
        M_blocks = str_to_blocks(M_padded)                       # split into mbl-bit blocks.         
        for block in M_blocks:                                   # for each message block...
            W = message_schedule(block)                          # obtain message schedule.
            working_variables = my_update_variables(W)           # obtain working variables.
            for j in range (8):                                  
                H[j] = (H[j]+ working_variables[j])&MASK         # update hash values (section 6.2.2-4.)
        
        if(form=="bin"):
            return ''.join(format(h, f'0{bl}b') for h in H) # convert final hash values into binary string.
    
        return ''.join(format(h, f'0{bl//4}x') for h in H) # convert final hash values into hex string.
        
    
    return main()
