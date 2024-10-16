# 512
from grp512.sigma512 import*
from grp512.constants import MASK

def str_to_bin(M):
    '''
    Takes in a string M and converts it to a binary string.
    '''
    Mbytes = M.encode()
    return ''.join(format(x,'08b') for x in Mbytes)
# ---------------------------------NIST document page 13, section 5.1.1.---------------------------------
def get_k(l):
    '''
    Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 896 mod 1024.
    '''
    n = (l+1)&1023           # & 1023 is equivalent to %1024
    return (896-n)&1023

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

def split_1024bit(M):
    '''
    Input: String of length 1024n for some n.
    Output: String array, M split into 1024bit blocks.
    '''
    if(len(M)&1023!=0):
        raise ValueError("Input string must have length 1024 for some n.")

    total_blocks = int(len(M)/1024)    # number of total blocks
    message_blocks = []               # array to store values
    for i in range (total_blocks):
        block = M[1024*i:1024*(i+1)]
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

# ---------------------------------Page 22, section 6.2.2.-1---------------------------------

def get_message_schedule(M):
    '''
    Input: String M of length 1024.
    Output: Array of 80 integers, message schedule as described in the NIST document
    '''
    W = split_64bit(M).copy()
    for t in range(16,80):
        Wt = (sig1(W[t-2]) + W[t-7] + sig0(W[t-15])+W[t-16])&MASK
        W.append(Wt)
    return W

if __name__=='__main__':
    nstr = "1"+"0"*63
    print(int(nstr,2))
    '''
    M = '1'
    M_padded = padding(M)
    assert(len(M_padded)==1024)
    assert(M_padded[8]=="1")
    assert(M_padded[-4:-1]+M_padded[-1]=="1000")
    '''