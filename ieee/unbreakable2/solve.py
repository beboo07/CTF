from pwn import *
from Crypto.Util.number import GCD,long_to_bytes
import gmpy2
n=[]
nn=[]
e=[]
cc=[]
c=[]
for i in range(150):
	r = remote('159.223.29.250', 1338  , level = 'debug')#lac.tf 31190

	n.append(int(r.recvline().decode().strip()[3:]))
	e.append(int(r.recvline().decode().strip()[3:]))
	c.append(int(r.recvline().decode().strip()[3:]))
	r.close()
z=e[:]
z.sort()

if z[0]<=z.count(z[0]):
	zz=z[0]
for i in range(len(e)):
	if i==zz:
		nn.append(n[i])
		cc.append(c[i])
print(long_to_bytes(gmpy2.iroot(crt(n,c)[0],zz)[0]))
		
