import constants
from basic_funcs import *
from get_hash import get_hash

def sha512(M):
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
            'K_constants': constants.K512,
            'initial_hash': constants.initial_hash_512, 
            's0':sig0, 
            's1':sig1, 
            'S0':Sig0, 
            'S1':Sig1, 
            'get_k': get_k
            }
    
    return get_hash(config, M)

# Take input from command line.
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

