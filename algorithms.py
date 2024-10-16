from sha_groups import *

# 256 Group
def sha224(M,form='hex'):
    initial_hash = [0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939,
                     0xffc00b31, 0x68581511, 0x64f98fa7,0xbefa4fa4]
    return grp256(224,initial_hash, M,form)

def sha256(M,form='hex'):
    initial_hash = [0x6a09e667, 0xbb67ae85,0x3c6ef372,0xa54ff53a, 
                    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    return grp256(256,initial_hash, M,form)

# 512 Group
def sha384(M,form='hex'):
    initial_hash = [0xcbbb9d5dc1059ed8, 0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939, 
           0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4]
    return grp512(384, initial_hash, M,form)

def sha512(M,form='hex'):
    initial_hash = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 
                    0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f, 
                    0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
    return grp512(512,initial_hash, M,form)

def sha_512_224(M,form='hex'):
    initial_hash = [0x8C3D37C819544DA2,0x73E1996689DCD4D6,0x1DFAB7AE32FF9C82,0x679DD514582F9FCF, 
    0x0F6D2B697BD44DA8,0x77E36F7304C48942,0x3F9D85A86A1D36C8,0x1112E6AD91D692A1]
    return grp512(224,initial_hash, M,form)

def sha_512_256(M,form='hex'):
   initial_hash = [0x22312194FC2BF72C,0x9F555FA3C84C64C2,0x2393B86B6F53B151, 
                0x963877195940EABD,0x96283EE2A88EFFE3,0xBE5E1E2553863992,
                0x2B0199FC2C85B8AA,0x0EB72DDC81C52CA2]
   return grp512(256,initial_hash,M,form)

if __name__=='__main__':
    for alg in (sha384, sha_512_224, sha_512_256):
        print(alg("hello world"))