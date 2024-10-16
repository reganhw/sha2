import random
from grp512.preprocessing import*

def test_get_k():
    for i in range (10):                 # For 20 random integers l,
        l = random.randint(0,10000)
        k = get_k(l)                     # get k and check:
        assert(0<=k)                     # k is non-negative
        assert(k<1024)                   # k is the smallest non-negative integer satisfying this
        assert(((k+1+l)%1024)==896)      # k+1+l :=896 mod 512