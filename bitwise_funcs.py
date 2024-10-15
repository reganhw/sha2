from constants import MASK

def neg(x):
    '''
    Takes in an integer x, and performs bitwise negation, while
    regarding x 32 bit.
    '''
    return x ^MASK                 

# ---------------------------------NIST document page 8, section 3.2.---------------------------------

def shr(n,x):
    '''
    Right-shifts integer x by n.
    '''
    return x>>n

def rotl(n,x):
    '''
    Left-rotates integer x by n.
    '''
    result = (x<<n) |(x>>(32-n))     # actual output
    return result & MASK             # keep under 32 bits

def rotr(n,x):
    '''
    Right-rotates integer x by n.
    '''
    result = (x>>n)|(x<<(32-n))      # actual output
    return result & MASK             # keep under 32 bits



