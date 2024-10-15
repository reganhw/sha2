from grp256 import grp256
from constants import *

def sha224(M, form = "hex"):
    '''
    Input: Message string M of any length.
    Output: The sha224 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    if(form=='bin'):
        return grp256.get_hash(M, initial_hash_224, "bin")[:224]
    else:
        return grp256.get_hash(M, initial_hash_224)[:56]

def sha256(M, form="hex"):
    return grp256.get_hash(M, initial_hash_256, form)

# Take input from command line.

if __name__ == '__main__':
    print(sha256("helloworld"))
