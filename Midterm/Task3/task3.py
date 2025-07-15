
# Task 3: Hashing and HMAC (Alternate Version)
from Crypto.Hash import SHA256, HMAC

# Original message
msg = b"Never trust, always verify."
with open("data_v2.txt", "wb") as f:
    f.write(msg)

# SHA-256 Hash
hash_obj = SHA256.new(msg)
print("SHA-256 Hash:", hash_obj.hexdigest())

# HMAC generation
key = b"secretkey123"
hmac = HMAC.new(key, digestmod=SHA256)
hmac.update(msg)
print("HMAC Original:", hmac.hexdigest())

# Tamper message and recompute
tampered = b"Never trost, always verify."
hmac_tampered = HMAC.new(key, digestmod=SHA256)
hmac_tampered.update(tampered)
print("HMAC Tampered:", hmac_tampered.hexdigest())

# Compare
if hmac.hexdigest() != hmac_tampered.hexdigest():
    print("HMAC check failed: Integrity compromised.")
else:
    print("HMAC check passed.")
