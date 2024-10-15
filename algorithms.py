from grp256 import grp256

def sha224(M, form = "hex"):
    '''
    Input: Message string M of any length.
    Output: The sha224 hash for M. If form=="bin" then the output is binary. Otherwise it's hex.
    '''
    return grp256.get_hash(M, 224, form)

def sha256(M, form="hex"):
    return grp256.get_hash(M, 256, form)

# Take input from command line.

if __name__ == '__main__':
    print(sha224("helloworld"))
