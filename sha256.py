import constants
from basic_funcs import *
from get_hash import get_hash

def get_k_256(l):
    '''
    Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 448 mod 512.
    '''
    n = (l+1)&511           # &511 is equivalent to %512
    return (448-n)&511

def sha256(M):
    def Sig0(x):
        return rotr(2,x)^ rotr(13,x)^rotr(22,x)

    def Sig1(x):
        return rotr(6,x)^rotr(11,x)^rotr(25,x)

    def sig0(x):
        return rotr(7,x)^rotr(18,x)^shr(3,x)

    def sig1(x):
        return rotr(17,x)^rotr(19,x)^shr(10,x)
  
    config = {
            'MASK':(1<<32)-1,
            'bl':32, 
            'mbl':512, 
            't_lim':64,
            'K_constants': constants.K256,
            'initial_hash': constants.initial_hash_256, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k_256
            }
    
    return get_hash(config, M)

# Take input from command line.
if __name__=='__main__':
    print(sha256("helloworld"))
