from bitwise_funcs import*
from grp512.preprocessing import*
from grp512.constants import *

def update_variables(W,H):
    '''
    Input - W: Message schedule W of a message. Array of 64 integers.
    Input - H: Hash values at the current stage. Array of 8 integers.
    Output - Array of integers [a,b,c,d,e,f,g,h] as in NIST document page 22, seciton 6.2.2.-3.
    '''
    a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
    for t in range (80):
        T1 = (h + Sig1(e) + Ch(e,f,g, MASK) +K512[t] + W[t])&MASK
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

def get_hash(M, form="hex"):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    M_padded = padding(M)                                    # pad M.
    M_blocks = split_1024bit(M_padded)                        # split into 512 bit blocks.
    H = initial_hash_512.copy()
                                                             # intialise hash.
    for block in M_blocks:                                   # for each message block...
        W = get_message_schedule(block)                      # obtain message schedule.
        working_variables = update_variables(W,H)            # obtain working variables.
        for j in range (8):                                  
            H[j] = (H[j]+ working_variables[j])&MASK         # update hash values (section 6.2.2-4.)
    
    if(form=="bin"):
        return ''.join(format(h, '064b') for h in H) # convert final hash values into binary string.
    
    return ''.join(format(h, '016x') for h in H) # convert final hash values into hex string.

if __name__ =='__main__':
    print(get_hash(''))