from constants import *
from bitwise_funcs import*
from preprocessing import*

def grp256(M, initial_hash, form="hex"):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    M_padded = padding(M)                                    # pad M.
    M_blocks = split_512bit(M_padded)                        # split into 512 bit blocks.
    H = initial_hash
                                                             # intialise hash.
    for block in M_blocks:                                   # for each message block...
        W = get_message_schedule(block)                      # obtain message schedule.
        working_variables = update_variables(W,H)            # obtain working variables.
        for j in range (8):                                  
            H[j] = (H[j]+ working_variables[j])&MASK         # update hash values (section 6.2.2-4.)
    
    if(form=="bin"):
        return ''.join(format(h, '032b') for h in H)         # convert final hash values into binary string.

    return ''.join(format(h, '08x') for h in H)              # convert final hash values into hex string.

def sha224(M, form = "hex"):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    initial_hash = [0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939, 0xffc00b31, 0x68581511, 0x64f98fa7,0xbefa4fa4]
    if(form=='bin'):
        return grp256(M, initial_hash, "bin")[:224]
    else:
        return grp256(M, initial_hash)[:56]

def update_variables(W,H):
    '''
    Input - W: Message schedule W of a message. Array of 64 integers.
    Input - H: Hash values at the current stage. Array of 8 integers.
    Output - Array of integers [a,b,c,d,e,f,g,h] as in NIST document page 22, seciton 6.2.2.-3.
    '''
    a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
    for t in range (64):
        T1 = (h + Sig1(e) + Ch(e,f,g) + K[t] + W[t])&MASK
        T2 = (Sig0(a) + Maj(a,b,c))&MASK
        h = g
        g = f
        f = e
        e = (d + T1)&MASK
        d = c
        c=b
        b=a
        a = (T1 + T2)&MASK
    return a,b,c,d,e,f,g,h

# Take input from command line.

if __name__ == '__main__':
    print(sha224("helloworld"))
