from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
from os import urandom

# Bob generates his RSA keypair
privkey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pubkey = privkey.public_key()
with open("public.pem", "wb") as f:
    f.write(pubkey.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
with open("private.pem", "wb") as f:
    f.write(privkey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))

# Alice writes a file
with open("alice_message.txt", "wb") as f:
    f.write(b"Exchange file with RSA+AES hybrid scheme.")

# Alice generates AES key and IV
a_key = urandom(32)
a_iv = urandom(16)
cipher = Cipher(algorithms.AES(a_key), modes.CBC(a_iv))
enc = cipher.encryptor()
with open("alice_message.txt", "rb") as f:
    plain = f.read()
padded = plain + b'\x01' * (16 - len(plain) % 16)
ciphertext = enc.update(padded) + enc.finalize()
with open("encrypted_file.bin", "wb") as f:
    f.write(a_iv + ciphertext)

# Alice encrypts AES key with Bob's public key
a_key_enc = pubkey.encrypt(
    a_key,
    padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
with open("aes_key_encrypted.bin", "wb") as f:
    f.write(a_key_enc)

# Bob decrypts AES key and file
dec_key = privkey.decrypt(a_key_enc, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
with open("encrypted_file.bin", "rb") as f:
    iv2 = f.read(16)
    ct = f.read()
decipher = Cipher(algorithms.AES(dec_key), modes.CBC(iv2))
dec = decipher.decryptor()
decrypted = dec.update(ct) + dec.finalize()
decrypted = decrypted.rstrip(b'\x01')
with open("decrypted_message.txt", "wb") as f:
    f.write(decrypted)

# Integrity check using SHA-256
orig_sha = hashlib.sha256(plain).hexdigest()
final_sha = hashlib.sha256(decrypted).hexdigest()
print("SHA-256 integrity check:", "PASS" if orig_sha == final_sha else "FAIL")
