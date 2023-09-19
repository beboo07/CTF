from Crypto.Util.number import long_to_bytes , GCD
import requests

burp0_url = "http://161.35.29.241:1336/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
n=[]
c=[]
e=65537
p=1
r=requests.get(burp0_url, headers=burp0_headers)
x=r.json()
n.append(x['n'])
c.append(x['c'])
while True:
	r=requests.get(burp0_url, headers=burp0_headers)
	x=r.json()
	nn=x['n']
	cc=x['c']
	for i in n:
		if GCD(i,nn)!= 1 and i != nn:
			p=GCD(i,nn)
			index=n.index(i)
	if p!=0:
		break
nn=n[index]
cc=c[index]
q=nn//p
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
print(long_to_bytes(pow(cc,d,nn)))
