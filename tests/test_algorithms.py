import hashlib
from main import *

special_chrs = " !\"£^ "

def alg_test(alg):
    s = ""
    for i in range(5):
        # Check hex version.
        hash_hex = alg(s)
        verified_func = getattr(hashlib, alg.__name__)  # hashlib.sha
        verified_hash_hex = verified_func(s.encode()).hexdigest()
        assert(hash_hex==verified_hash_hex)

        # Check bin version.
        bin_length = len(hash_hex)*4
        hash_bin = alg(s,'bin')
        verified_hash_bin = format(int(verified_hash_hex,16), f'0{bin_length}b')
        assert(hash_bin==verified_hash_bin)
        
        # Update s to be: (current string) + (its hash) + (a special chr).
        s = s + hash_hex + special_chrs[i]


def test_sha256():
    alg_test(sha256)


def test_sha224():
    alg_test(sha224)


def test_sha512():
    alg_test(sha512)


