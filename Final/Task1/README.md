# Encrypted Messaging App Prototype

**Workflow:**
1. User A generates RSA key pair and shares public key.
2. User B creates a message, encrypts it with a new AES-256 key and IV.
3. AES key is encrypted using User A’s public RSA key and sent with the ciphertext.
4. User A uses their private RSA key to decrypt the AES key, and then decrypts the message.

**File descriptions:**
- message.txt: Original plaintext message.
- encrypted_message.bin: Encrypted message (AES-256, with IV prepended).
- aes_key_encrypted.bin: Encrypted AES key (using RSA).
- decrypted_message.txt: Final decrypted message.

**Purpose:**  
This workflow ensures both strong symmetric encryption (AES) and secure key transport (RSA).
