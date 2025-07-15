
# Task 2: ECC Key Generation, Signing, and Verification (Alternate Version)
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generate ECC keys using P-256
ecc_key = ECC.generate(curve='P-256')
with open("ecc_private.pem", "wt") as f:
    f.write(ecc_key.export_key(format='PEM'))
with open("ecc_public.pem", "wt") as f:
    f.write(ecc_key.public_key().export_key(format='PEM'))

# Sign message
message = b"Elliptic Curves are efficient."
with open("ecc.txt", "wb") as f:
    f.write(message)

hash_obj = SHA256.new(message)
signer = DSS.new(ecc_key, 'fips-186-3')
signature = signer.sign(hash_obj)

with open("signature.bin", "wb") as f:
    f.write(signature)

# Verify
pub_key = ECC.import_key(open("ecc_public.pem").read())
verifier = DSS.new(pub_key, 'fips-186-3')
try:
    verifier.verify(SHA256.new(message), signature)
    print("Signature verified.")
except ValueError:
    print("Signature failed.")
