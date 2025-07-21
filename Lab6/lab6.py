from binascii import unhexlify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

BLOCK_SIZE = 16
KEY = b"this_is_16_bytes"

CIPHERTEXT_HEX = (
    "746869735f69735f31365f6279746573"
    "9404628dcdf3f003482b3b0648bd920b"
    "3f60e13e89fa6950d3340adbbbb41c12"
    "b3d1d97ef97860e9df7ec0d31d13839a"
    "e17b3be8f69921a07627021af16430e1"
)


def padding_oracle(ciphertext: bytes) -> bool:
    """Returns True if ciphertext decrypts with valid padding, False otherwise."""
    if len(ciphertext) % BLOCK_SIZE != 0:
        return False
    try:
        iv = ciphertext[:BLOCK_SIZE]
        ct = ciphertext[BLOCK_SIZE:]
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(ct) + decryptor.finalize()
        unpadder = padding.PKCS7(BLOCK_SIZE * 8).unpadder()
        unpadder.update(decrypted)
        unpadder.finalize()
        return True
    except (ValueError, TypeError):
        return False


def split_blocks(data: bytes, block_size: int = BLOCK_SIZE) -> list[bytes]:
    """Divide byte data into a list of equally sized blocks."""
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]


def decrypt_block(prev_block: bytes, target_block: bytes) -> bytes:
    """Apply padding oracle attack logic to decrypt a single ciphertext block."""
    intermediate_vals = bytearray(BLOCK_SIZE)
    decrypted_bytes = bytearray(BLOCK_SIZE)

    for position in reversed(range(BLOCK_SIZE)):
        pad_byte = BLOCK_SIZE - position
        for potential in range(256):
            crafted_prefix = bytearray(b'\x00' * position)

            for idx in range(position + 1, BLOCK_SIZE):
                crafted_prefix.append(intermediate_vals[idx] ^ pad_byte)
            crafted_prefix.append(potential ^ pad_byte)

            test_input = bytes(crafted_prefix) + target_block
            if padding_oracle(test_input):
                intermediate_vals[position] = potential ^ pad_byte
                decrypted_bytes[position] = intermediate_vals[position] ^ prev_block[position]
                break
    return bytes(decrypted_bytes)


def padding_oracle_attack(ciphertext: bytes) -> bytes:
    """Orchestrate full decryption using the padding oracle attack."""
    ct_blocks = split_blocks(ciphertext)
    plaintext = bytearray()

    for idx in range(1, len(ct_blocks)):
        decrypted = decrypt_block(ct_blocks[idx - 1], ct_blocks[idx])
        plaintext.extend(decrypted)

    return bytes(plaintext)


def unpad_and_decode(plaintext: bytes) -> str:
    """Safely remove padding and decode plaintext, fallback if needed."""
    try:
        unpadder = padding.PKCS7(BLOCK_SIZE * 8).unpadder()
        return (unpadder.update(plaintext) + unpadder.finalize()).decode('utf-8')
    except Exception:
        trimmed = plaintext.rstrip(bytes(range(1, 17)))
        return trimmed.decode('utf-8', errors='replace')


if __name__ == "__main__":
    try:
        ciphertext = unhexlify(CIPHERTEXT_HEX)
        print(f"[*] Ciphertext length: {len(ciphertext)} bytes")
        print(f"[*] IV: {ciphertext[:BLOCK_SIZE].hex()}")
        recovered = padding_oracle_attack(ciphertext)
        print("\n[+] Decryption complete!")
        print(f" Recovered plaintext (raw bytes): {recovered}")
        print(f" Hex: {recovered.hex()}")
        decoded = unpad_and_decode(recovered)
        print("\n Final plaintext:")
        print(decoded)
    except Exception as e:
        print(f"\n Error occurred: {e}")
