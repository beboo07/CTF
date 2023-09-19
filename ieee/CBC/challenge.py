from Crypto.Cipher import AES

key = b"9Y3RjZ%c(5W!****"
iv = b"****************"

cipher  = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
print(cipher.encrypt(b"!Super secret encrypted message!").hex())
