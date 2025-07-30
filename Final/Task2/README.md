# Secure File Exchange Using RSA + AES

Steps:
- Bob generates RSA keys (public.pem/private.pem).
- Alice writes alice_message.txt, encrypts with AES-256, IV prepended to encrypted_file.bin.
- AES key is encrypted with RSA and written to aes_key_encrypted.bin.
- Bob decrypts the AES key and then the file, restoring decrypted_message.txt.
- Integrity is verified by comparing SHA-256 hashes of original and decrypted file.

**Deliverables:** alice_message.txt, encrypted_file.bin, aes_key_encrypted.bin, decrypted_message.txt, public.pem, private.pem
