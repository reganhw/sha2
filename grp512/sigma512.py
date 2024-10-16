from bitwise_funcs import *
from grp512.constants512 import MASK
# ---------------------------------Page 10, section 4.1.2.---------------------------------

def Sig0(x):
    return rotr(28,x,MASK)^ rotr(34,x,MASK)^rotr(39,x,MASK)

def Sig1(x):
    return rotr(14,x,MASK)^rotr(18,x,MASK)^rotr(41,x,MASK)

def sig0(x):
    return rotr(1,x,MASK)^rotr(18,x,MASK)^shr(7,x,MASK)

def sig1(x):
    return rotr(19,x,MASK)^rotr(61,x,MASK)^shr(6,x,MASK)