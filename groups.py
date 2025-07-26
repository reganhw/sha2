from constants import *
from sha2 import *

def grp256(initial_hash, M, output_length = 256, form='hex'):
    '''
    General form for SHA256 and SHA224.
    '''
    MASK = (1<<32)-1    # 32 1s in binary

    # Sigma funcs: NIST document, section 4.1.2, page 10.
    def Sig0(x):
        return rotr(2,x, MASK)^ rotr(13,x, MASK)^rotr(22,x,MASK)

    def Sig1(x):
        return rotr(6,x, MASK)^rotr(11,x, MASK)^rotr(25,x, MASK)

    def sig0(x):
        return rotr(7,x, MASK)^rotr(18,x, MASK)^shr(3,x)

    def sig1(x):
        return rotr(17,x, MASK)^rotr(19,x, MASK)^shr(10,x)
    
    # Section 5.1.1, page 13.
    def get_k(l):
        '''
        Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 448 mod 512.
        '''
        n = (l+1)&511           # &511 is equivalent to %512
        return (448-n)&511
    
    config = {
            'MASK':MASK,        
            'bl':32,                               # Section 1, page 1.
            'mbl':512,                             # Section 1, page 1.
            't_lim':64,                            # Section 6.2.2, page 23.
            'K_constants': K256,
            'initial_hash': initial_hash, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k
            }
    
    return sha2(config,M,output_length,form)   # cut to appropriate length

def grp512(initial_hash, M, output_length = 512, form='hex'):
    '''
    General form for SHA512,SHA384, SHA512/224, and SHA512/256.
    '''
    MASK = (1<<64)-1    # 64 1s in binary

    # Section 4.1.3, page 11.
    def Sig0(x):
        return rotr(28,x,MASK)^ rotr(34,x,MASK)^rotr(39,x,MASK)

    def Sig1(x):
        return rotr(14,x,MASK)^rotr(18,x,MASK)^rotr(41,x,MASK)

    def sig0(x):
        return rotr(1,x,MASK)^rotr(8,x,MASK)^shr(7,x)

    def sig1(x):
        return rotr(19,x,MASK)^rotr(61,x,MASK)^shr(6,x)
    
     # Section 5.1.2, page 13.
    def get_k(l):
        '''
        Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 896 mod 1024.
        '''
        n = (l+1)&1023           # & 1023 is equivalent to %1024
        return (896-n)&1023
    
    config = {
            'MASK':MASK,
            'bl':64,                          # Section 1, page 1. 
            'mbl':1024,                       # Section 1, page 1.
            't_lim':80,                       # Section 6.4.2, page 24.
            'K_constants': K512,
            'initial_hash': initial_hash, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k
            }
    
    return sha2(config,M,output_length,form)
