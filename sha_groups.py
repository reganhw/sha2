from constants import *
from basic_funcs import *
from get_hash import get_hash

def grp256(output_length, initial_hash, M,form='hex'):
    def Sig0(x):
        return rotr(2,x)^ rotr(13,x)^rotr(22,x)

    def Sig1(x):
        return rotr(6,x)^rotr(11,x)^rotr(25,x)

    def sig0(x):
        return rotr(7,x)^rotr(18,x)^shr(3,x)

    def sig1(x):
        return rotr(17,x)^rotr(19,x)^shr(10,x)
    
    def get_k(l):
        '''
        Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 448 mod 512.
        '''
        n = (l+1)&511           # &511 is equivalent to %512
        return (448-n)&511
  
    config = {
            'MASK':(1<<32)-1,
            'bl':32, 
            'mbl':512, 
            't_lim':64,
            'K_constants': K256,
            'initial_hash': initial_hash, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k
            }
    
    h = get_hash(config,M,form)            # get hash
    hlen = len(h)
    return h[:int(hlen*(output_length/256))]   # cut to appropriate length

def grp512(output_length, initial_hash, M,form='hex'):
    MASK = (1<<64)-1
    def Sig0(x):
        return rotr(28,x,MASK)^ rotr(34,x,MASK)^rotr(39,x,MASK)

    def Sig1(x):
        return rotr(14,x,MASK)^rotr(18,x,MASK)^rotr(41,x,MASK)

    def sig0(x):
        return rotr(1,x,MASK)^rotr(8,x,MASK)^shr(7,x)

    def sig1(x):
        return rotr(19,x,MASK)^rotr(61,x,MASK)^shr(6,x)

    def get_k(l):
        '''
        Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 896 mod 1024.
        '''
        n = (l+1)&1023           # & 1023 is equivalent to %1024
        return (896-n)&1023
  
    config = {
            'MASK':MASK,
            'bl':64, 
            'mbl':1024, 
            't_lim':80,
            'K_constants': K512,
            'initial_hash': initial_hash, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k
            }
    
    h = get_hash(config,M,form)          # get hash
    hlen = len(h)
    return h[:int(hlen*(output_length/256))] # cut to appropriate length
