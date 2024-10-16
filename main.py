# Initial hashes can be seen in: NIST document, section 5.3, pages 14-16.
from groups import *

def sha224(M,form='hex'): 
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA224 hash of M in form 'form'.
    Reference: NIST document, section 6.3, pages 23-24.
    '''

    initial_hash = [0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939,
                     0xffc00b31, 0x68581511, 0x64f98fa7,0xbefa4fa4]
    
    return grp256(initial_hash, M,output_length = 224, form=form)

def sha256(M,form='hex'):
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA256 hash of M in form 'form'.
    Reference: See groups.py -> grp256.
    ''' 
    initial_hash = [0x6a09e667, 0xbb67ae85,0x3c6ef372,0xa54ff53a, 
                    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    
    return grp256(initial_hash, M,form=form)

def sha384(M,form='hex'):  # 
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA384 hash of M in form 'form'.
    Reference: Section 6.5, page 26.
    '''
    initial_hash = [0xcbbb9d5dc1059ed8, 0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939, 
           0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4]
    
    return grp512(initial_hash, M,output_length = 384, form=form)

def sha512(M,form='hex'):
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA512 hash of M in form 'form'.
    Reference: See groups.py -> grp512.
    '''

    initial_hash = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 
                    0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f, 
                    0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
    
    return grp512(initial_hash, M,form=form)

def sha_512_224(M,form='hex'):
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA512/224 hash of M in form 'form'.
    Reference: Section 6.6, page 26.
    '''
    initial_hash = [0x8C3D37C819544DA2,0x73E1996689DCD4D6,0x1DFAB7AE32FF9C82,0x679DD514582F9FCF, 
    0x0F6D2B697BD44DA8,0x77E36F7304C48942,0x3F9D85A86A1D36C8,0x1112E6AD91D692A1]

    return grp512(initial_hash, M,output_length=224,form=form)

def sha_512_256(M,form='hex'): 
    '''
    Input: Message 'M' of any length, optional input 'form' which is either 'hex' or 'bin'.
    Output: SHA512/256 hash of M in form 'form'.
    Reference: Section 6.7, page 26.
    '''

    initial_hash = [0x22312194FC2BF72C,0x9F555FA3C84C64C2,0x2393B86B6F53B151, 
                0x963877195940EABD,0x96283EE2A88EFFE3,0xBE5E1E2553863992,
                0x2B0199FC2C85B8AA,0x0EB72DDC81C52CA2]
   
    return grp512(initial_hash,M, output_length=256, form=form)

if __name__=='__main__':
    message = input("\n  Input: ")
    print("")
    print("--SHA224: ", sha224(message))
    print("--SHA256: ", sha256(message))
    print("--SHA384: ", sha384(message))
    print("--SHA512: ", sha512(message))
    print("--SHA512/224: ", sha_512_224(message))
    print("--SHA512/256: ", sha_512_256(message))