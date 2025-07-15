# Task 1: AES-128-CBC Encryption and Decryption (Alternate Version)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# File setup
plaintext = b"This file contains top secret information."
with open("secret.txt", "wb") as f:
    f.write(plaintext)

# AES-128-CBC Encryption
key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

with open("secret.enc", "wb") as f:
    f.write(iv + ciphertext)

# AES-128-CBC Decryption
with open("secret.enc", "rb") as f:
    data = f.read()
    iv_dec, ct = data[:16], data[16:]

decipher = AES.new(key, AES.MODE_CBC, iv_dec)
decrypted = unpad(decipher.decrypt(ct), AES.block_size)

with open("secret_decrypted.txt", "wb") as f:
    f.write(decrypted)
