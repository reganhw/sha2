from sha_groups import *
from constants import *

def sha224(M,form='hex'):
    return grp256(224,M,form)

def sha256(M,form='hex'):
    return grp256(256,M,form)

def sha512(M,form='hex'):
    return grp512(512,M,form)



