This challenge was goal was to get the right iv that was used to encrypt this data u have a known plaintext with 32 bytes len and partial key with the last 4 bytes not known and partial ciphertext 

first u will need to know what does AES-CBC work so here is an image that explain how does it work 
![image](https://github.com/beboo07/CTF/assets/103918753/1f5dce9c-12dd-4e00-8bbe-89551e484598)

so first we need to make the ciphertext we have into two parts and we have the second part full and we also know the plaintext of this part so the only missing values is the first ciphertext and the 4 bytes in the key 

we have some bytes from the first ciphertext that is used to xor the plaintext before encrypted so if we just decrypt the 2nd block with the right key making the iv =b'\0'*16 so when xor with pt it will not alterd it and xored it with 2nd block in plaintext we should get the same starts and end bytes in the 1st block 
by this we will brute force the 4 bytes and check for the equation using string.printable
and we get two keys that will generate the 1st ct with this known bytes 
![image](https://github.com/beboo07/CTF/blob/main/ieee/CBC/image.png?raw=true)
i took the first key and worked with the 1st block 
know to get iv =pt ^ D(ct1) 
and we got ct1 and key from the first step so now we can get iv and it worked 
![image](https://github.com/beboo07/CTF/blob/main/ieee/CBC/flag.png?raw=true)
