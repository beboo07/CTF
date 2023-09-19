from Crypto.Cipher import AES

zz=b'!Super secret en'
c0=198
c16=137
c15=117
strr="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "
key='9Y3RjZ%c(5W!8MH%'
iv=b'\0'*16

cipher  = AES.new(key=key.encode(), iv=iv, mode=AES.MODE_CBC)
z=cipher.decrypt(bytes.fromhex('c6659d07443ee312fa4eaabc6d407589'))
c=''			
for i in range(len(z)):
	cc=hex(z[i]^zz[i])[2:]
	if len(cc)!=2:
		cc='0'+cc
	c+=cc
print(c)
print(bytes.fromhex(c))


#keys

#9Y3RjZ%c(5W!8MH%
#c1=c6659d07443ee312fa4eaabc6d407589


#9Y3RjZ%c(5W!9vcr
#c1=c68b3cadac3cea8400e586d89fd67589








