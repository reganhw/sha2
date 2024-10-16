import grp512.constants as constants512
import grp512.sigma512 as sigma512
from get_hash import get_hash
'''
def sha224(M, form = "hex"):
    return grp256.get_hash(M, 224, form)

def sha256(M, form="hex"):
    return grp256.get_hash(M, 256, form)

def sha512(M, form="hex"):
    return grp512.get_hash(M,form)
'''
def get_k_512(l):
    '''
    Takes in integer l and returns k, the smallest non-negative integer satisfying l+1+k = 896 mod 1024.
    '''
    n = (l+1)&1023           # & 1023 is equivalent to %1024
    return (896-n)&1023

def sha512(M):
  
    config = {
            'bl':64, 
            'mbl':1024, 
            't_lim':80,
            'K_constants': constants512.K512,
            'initial_hash': constants512.initial_hash_512, 
            's0':sigma512.sig0, 
            's1':sigma512.sig1, 
            'S0':sigma512.Sig0, 
            'S1':sigma512.Sig1, 
            'get_k': get_k_512
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

