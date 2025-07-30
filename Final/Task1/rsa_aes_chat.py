# Task 1: Encrypted Messaging App
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

# User A generates key pair
rsa_priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
rsa_pub = rsa_priv.public_key()

# User B creates and writes a message
msg = b"Team communication secured by hybrid encryption."
with open("message.txt", "wb") as f:
    f.write(msg)

# User B encrypts the message using AES-256
aes_key = urandom(32)
aes_iv = urandom(16)
aes_cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_iv))
aes_enc = aes_cipher.encryptor()
msg_padded = msg + b'\x00' * (16 - len(msg) % 16)
enc_msg = aes_enc.update(msg_padded) + aes_enc.finalize()
with open("encrypted_message.bin", "wb") as f:
    f.write(aes_iv + enc_msg)

# AES key is encrypted using RSA
aes_key_enc = rsa_pub.encrypt(
    aes_key,
    padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
with open("aes_key_encrypted.bin", "wb") as f:
    f.write(aes_key_enc)

# User A decrypts the AES key
aes_key_dec = rsa_priv.decrypt(
    aes_key_enc,
    padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# User A decrypts the message
aes_cipher2 = Cipher(algorithms.AES(aes_key_dec), modes.CBC(aes_iv))
aes_dec = aes_cipher2.decryptor()
dec_msg = aes_dec.update(enc_msg) + aes_dec.finalize()
dec_msg = dec_msg.rstrip(b'\x00')
with open("decrypted_message.txt", "wb") as f:
    f.write(dec_msg)
