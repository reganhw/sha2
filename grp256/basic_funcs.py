from bitwise_funcs import *
# ---------------------------------Page 10, section 4.1.2.---------------------------------

def Ch(x,y,z):
    '''
    Input: Integers x,y,z such that 0<=x,y,z <=2**32-1
    Output: For 0<=i<=31,
    if x[i] = 1 -> output[i] = y[i]
    if x[i] = 0 -> output[i] = z[i]
    '''
    return (x & y) ^ (neg(x) & z)  

def Maj(x,y,z):
    '''
    Input: Integers x,y,z such that 0<=x,y,z <=2**32-1
    Output: For 0<=i<=31,
    if more than two of x[i],y[i],z[i] is 1 -> output[i]=1
    else -> output[i] =0
    '''
    return (x & y) ^(x & z) ^(y &z)

def Sig0(x):
    return rotr(2,x)^ rotr(13,x)^rotr(22,x)

def Sig1(x):
    return rotr(6,x)^rotr(11,x)^rotr(25,x)

def sig0(x):
    return rotr(7,x)^rotr(18,x)^shr(3,x)

def sig1(x):
    return rotr(17,x)^rotr(19,x)^shr(10,x)