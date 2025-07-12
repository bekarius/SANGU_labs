import subprocess
import os

# Step 1: Create original plaintext file
with open("original_message.txt", "w") as file:
    file.write("Hello! This file contains confidential information for cryptography lab exercises.\n")

# Step 2: RSA Key Pair Generation
subprocess.run(["openssl", "genrsa", "-out", "private_key.pem", "2048"])
subprocess.run(["openssl", "rsa", "-in", "private_key.pem", "-pubout", "-out", "public_key.pem"])

# Step 3: RSA Encryption
subprocess.run(["openssl", "rsautl", "-encrypt", "-pubin", "-inkey", "public_key.pem",
                "-in", "original_message.txt", "-out", "rsa_encrypted_message.bin"])

# Step 4: RSA Decryption
subprocess.run(["openssl", "rsautl", "-decrypt", "-inkey", "private_key.pem",
                "-in", "rsa_encrypted_message.bin", "-out", "rsa_decrypted_message.txt"])

# Step 5: AES Key and IV Generation
subprocess.run(["openssl", "rand", "-out", "aes_key.bin", "32"])
subprocess.run(["openssl", "rand", "-out", "aes_iv.bin", "16"])

# Step 6: AES Encryption (AES-256-CBC)
aes_key_hex = open("aes_key.bin", "rb").read().hex()
aes_iv_hex = open("aes_iv.bin", "rb").read().hex()

subprocess.run(["openssl", "enc", "-aes-256-cbc", "-in", "original_message.txt",
                "-out", "aes_encrypted_message.bin", "-K", aes_key_hex, "-iv", aes_iv_hex])

# Step 7: AES Decryption
subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-in", "aes_encrypted_message.bin",
                "-out", "aes_decrypted_message.txt", "-K", aes_key_hex, "-iv", aes_iv_hex])

# Step 8: RSA vs AES comparison
comparison_text = """
RSA vs AES Encryption:

Performance:
- RSA encryption and decryption are computationally intensive and slower.
- AES is optimized for speed and suitable for encrypting large data volumes quickly.

Use-cases:
- RSA is ideal for securely exchanging small data (e.g., AES keys, passwords) and digital signatures.
- AES is commonly used for efficiently encrypting files, databases, and large datasets.

Real-world scenarios combine RSA (for secure key exchange) with AES (for bulk data encryption).
"""

with open("rsa_aes_comparison.txt", "w") as file:
    file.write(comparison_text.strip())

print("Encryption and decryption tasks completed successfully.")