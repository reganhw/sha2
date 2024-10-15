import hashlib
from algorithms import *

special_chrs = " !\"£^ "

def test_sha256():
    s = ""
    for i in range(5):
        # Check hex version.
        hash_hex = sha256(s)
        verified_hash_hex = hashlib.sha256(s.encode()).hexdigest()

        # Check bin version.
        hash_bin = sha256(s,'bin')
        verified_hash_bin = format(int(verified_hash_hex,16), '0256b')
        assert(hash_bin==verified_hash_bin)
        
        # Update s.
        s = s+hash_hex+special_chrs[i]

if __name__=='__main__':
    s = sha256("")+" "
    print(sha256('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b8556'))