from sha_groups import *


def sha224(M,form='hex'):
    initial_hash = [0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939,
                     0xffc00b31, 0x68581511, 0x64f98fa7,0xbefa4fa4]
    return grp256(224,initial_hash, M,form)

def sha256(M,form='hex'):
    initial_hash = [0x6a09e667, 0xbb67ae85,0x3c6ef372,0xa54ff53a, 
                    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    return grp256(256,initial_hash, M,form)

def sha512(M,form='hex'):
    initial_hash = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 
                    0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f, 
                    0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
    return grp512(512,initial_hash, M,form)



