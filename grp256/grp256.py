from bitwise_funcs import*
from grp256.preprocessing import*
from grp256.constants import *

def update_variables(W,H):
    '''
    Input - W: Message schedule W of a message. Array of 64 integers.
    Input - H: Hash values at the current stage. Array of 8 integers.
    Output - Array of integers [a,b,c,d,e,f,g,h] as in NIST document page 22, seciton 6.2.2.-3.
    '''
    a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
    for t in range (64):
        T1 = (h + Sig1(e) + Ch(e,f,g) +K256[t] + W[t])&MASK
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

def get_hash(M, length, form="hex"):
    '''
    Input: Message string M of any length.
    Output: The sha256 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    M_padded = padding(M)                                    # pad M.
    M_blocks = split_512bit(M_padded)                        # split into 512 bit blocks.
    H = hashmap[length]
                                                             # intialise hash.
    for block in M_blocks:                                   # for each message block...
        W = get_message_schedule(block)                      # obtain message schedule.
        working_variables = update_variables(W,H)            # obtain working variables.
        for j in range (8):                                  
            H[j] = (H[j]+ working_variables[j])&MASK         # update hash values (section 6.2.2-4.)
    
    if(form=="bin"):
        return ''.join(format(h, '032b') for h in H)[:length] # convert final hash values into binary string.
    
    hex_length = 64*length//256
    return ''.join(format(h, '08x') for h in H)[:hex_length]  # convert final hash values into hex string.

