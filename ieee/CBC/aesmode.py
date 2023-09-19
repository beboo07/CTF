from Crypto.Cipher import AES
#result = bytes(x ^ y for x, y in zip(byte1, byte2))
zz=b'crypted message!'
c0=198
#7589
c15=137
c16=117
strr="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ "
k='9Y3RjZ%c(5W!'
iv=b'\0'*16
print(iv)
for i0 in strr:
	print(i0)
	for i1 in strr:
		for i2 in strr:
			for i3 in strr:
				key=k+i0+i1+i2+i3
				cipher  = AES.new(key=key.encode(), iv=iv, mode=AES.MODE_CBC)
				z=cipher.decrypt(bytes.fromhex('60cff0ad876f305be5359ebc5ec5dee4'))
				
				res=bytes(xxx ^ yyy for xxx, yyy in zip(z, zz)).hex()
				if res.startswith('c6') and res.endswith('7589'):
					print(res,key)
				
