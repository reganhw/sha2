# Tests for basic_funcs
import random
from basic_funcs import *

mask_32 = (1 << 32) - 1
mask_64 = ( 1<< 64) - 1

def neg_test(mask):
    for i in range (10):
        x = random.randint(0,mask)   # For a random integer x,
        negx = neg(x,mask)
        assert(x^negx == mask)       # x ^ neg(x) should equal a 32/64bit string of 1s.

def rot_test(bit_length, mask):
    for i in range (10):
        x = random.randint(0,mask)                          # For a random integer x,
        n = random.randint(0,bit_length-1)                  # and random n,
        assert(rotl(n,x,mask)==rotr(bit_length-n,x,mask))   # rotl(n,x) = rotr((bit_length-n,x)).

def Ch_test(bit_length,mask):
    for i in range (10):
        # Get random integers and calculate Ch(x,y,z)
        x = random.randint(0,mask)
        y = random.randint(0,mask)
        z = random.randint(0,mask)
        ch = Ch(x,y,z,mask)

        # Convert to bit string
        xb = format(x, f'0{bit_length}b')
        yb = format(y, f'0{bit_length}b')
        zb = format(z, f'0{bit_length}b')
        chb = format(ch, f'0{bit_length}b')
        
        # Check condition holds.
        for j in range(bit_length):            
            if(xb[j]=='1'):            # if x[i] = 1...
                assert(chb[j]==yb[j])  # output[i]=y[i]
            else:                      # if x[i] = 0...
                assert(chb[j]==zb[j])  # output[i]=z[i]

def Maj_test(bit_length,mask):
    for i in range (10):
        # Get random integers and calculate Maj(x,y,z).
        x = random.randint(0,mask)
        y = random.randint(0,mask)
        z = random.randint(0,mask)
        maj = Maj(x,y,z)

        # Convert to bit string.
        xb = format(x, f'0{bit_length}b')
        yb = format(y, f'0{bit_length}b')
        zb = format(z, f'0{bit_length}b')
        majb = format(maj, f'0{bit_length}b')
        
        # Check condition holds.
        for j in range(bit_length):
            if((int(xb[j])+ int(yb[j])+ int(zb[j]))>1): # if more than two of x[i],y[i],z[i] is 1...
                assert(majb[j]=="1")                    # output[i]=1
            else:                                       # else...
                assert(majb[j]=="0")                    # output[i]= 0

# 32-bit case
def test_neg_32():
    neg_test(mask_32)

def test_rot_32():
    rot_test(32,mask_32)

def test_Ch_32():
    Ch_test(32, mask_32)

def test_Maj_32():
    Maj_test(32,mask_32)

# 64-bit case
def test_neg_64():
    neg_test(mask_64)

def test_rot_64():
    rot_test(64, mask_64)

def test_Ch_64():
    Ch_test(64,mask_64)

def test_Maj_64():
    Maj_test(64,mask_64)

