import hashlib
import json

def compute_all_hashes(filepath):
    """Return dict of SHA-256, SHA-1, and MD5 hashes for a given file."""
    with open(filepath, "rb") as f:
        data = f.read()
    return {
        "SHA-256": hashlib.sha256(data).hexdigest(),
        "SHA-1": hashlib.sha1(data).hexdigest(),
        "MD5": hashlib.md5(data).hexdigest()
    }

# 1. Compute and store hashes for the original file
original_hashes = compute_all_hashes("original.txt")
with open("hashes.json", "w") as outfile:
    json.dump(original_hashes, outfile, indent=4)

# 2. Simulate tampering: the file tampered.txt should differ from original.txt
tampered_hashes = compute_all_hashes("tampered.txt")

# 3. Compare and flag if files differ
if tampered_hashes == original_hashes:
    print("Integrity check result: PASS")
else:
    print("Integrity check result: FAIL (file may have been tampered with!)")
