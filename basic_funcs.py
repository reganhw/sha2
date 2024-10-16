mask_32 = (1 << 32) - 1
mask_to_bits = {mask_32 : 32, (1<<64)-1 :64}

def neg(x, mask = mask_32):
    '''
    Takes in an integer x, and performs bitwise negation, while
    regarding x 32 bit.
    '''
    return x ^mask                 

# ---------------------------------NIST document page 8, section 3.2.---------------------------------

def shr(n,x):
    '''
    Right-shifts integer x by n.
    '''
    return x>>n

def rotl(n,x, mask = mask_32):
    '''
    Left-rotates integer x by n.
    '''
    lb = mask_to_bits[mask]
    result = (x<<n) |(x>>(lb-n))     # actual output
    return result & mask             # keep under 32 bits

def rotr(n,x, mask = mask_32):
    '''
    Right-rotates integer x by n.
    '''
    lb = mask_to_bits[mask]
    result = (x>>n)|(x<<(lb-n))      # actual output
    return result & mask             # keep under 32 bits



# ---------------------------------Page 10, section 4.1.2.---------------------------------

def Ch(x,y,z, mask = mask_32):
    '''
    Input: Integers x,y,z such that 0<=x,y,z <=2**32-1
    Output: For 0<=i<=31,
    if x[i] = 1 -> output[i] = y[i]
    if x[i] = 0 -> output[i] = z[i]
    '''
    return (x & y) ^ (neg(x,mask) & z)  

def Maj(x,y,z):
    '''
    Input: Integers x,y,z such that 0<=x,y,z <=2**32-1
    Output: For 0<=i<=31,
    if more than two of x[i],y[i],z[i] is 1 -> output[i]=1
    else -> output[i] =0
    '''
    return (x & y) ^(x & z) ^(y &z)

def str_to_bin(M):
    '''
    Takes in a string M and converts it to a binary string.
    '''
    Mbytes = M.encode()
    return ''.join(format(x,'08b') for x in Mbytes)