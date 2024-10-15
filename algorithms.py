from bitwise_funcs import*
from preprocessing import*
from constants import *

class Form256:
    def __init__(self, msg):
        self.msg = msg
        self.constants = K
        self.initial_hash = initial_hash
        self.hash = Form256.get_hash(msg)
    
    def __repr__(self):
        return self.hash

    def preprocess(M):
        return split_512bit(padding(M))
    
    def update_variables(W,H):
        '''
        Input - W: Message schedule W of a message. Array of 64 integers.
        Input - H: Hash values at the current stage. Array of 8 integers.
        Output - Array of integers [a,b,c,d,e,f,g,h] as in NIST document page 22, seciton 6.2.2.-3.
        '''
        a,b,c,d,e,f,g,h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
        for t in range (64):
            T1 = (h + Sig1(e) + Ch(e,f,g) + K[t] + W[t])&MASK
            T2 = (Sig0(a) + Maj(a,b,c))&MASK
            h = g
            g = f
            f = e
            e = (d + T1)&MASK
            d = c
            c=b
            b=a
            a = (T1 + T2)&MASK
        return a,b,c,d,e,f,g,h
    
    @staticmethod
    def get_hash(msg):
        return f"Hash for message {msg}. "

        
