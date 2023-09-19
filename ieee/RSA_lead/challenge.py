from Crypto.Util.number import getStrongPrime, bytes_to_long, long_to_bytes
import os

FLAG = b"IEEE{XXXX}"

p, q = getStrongPrime(512), getStrongPrime(512)
N = p*q
e = 3

phi = (p-1) * (q-1)
d = pow(e, -1, phi)
p1 = bytes_to_long(FLAG)

c = pow(p1, e, N) 
lead = (c % (2**512))
print(lead)