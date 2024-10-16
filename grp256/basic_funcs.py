from bitwise_funcs import *
# ---------------------------------Page 10, section 4.1.2.---------------------------------

def Sig0(x):
    return rotr(2,x)^ rotr(13,x)^rotr(22,x)

def Sig1(x):
    return rotr(6,x)^rotr(11,x)^rotr(25,x)

def sig0(x):
    return rotr(7,x)^rotr(18,x)^shr(3,x)

def sig1(x):
    return rotr(17,x)^rotr(19,x)^shr(10,x)