
# Task 4: Simulate Diffie-Hellman Key Exchange (Alternate Version)
from Crypto.Random import random

# Agreed parameters
p = 23  # small prime
g = 5   # primitive root mod 23

# Alice
a = random.randint(1, p-2)
A = pow(g, a, p)

# Bob
b = random.randint(1, p-2)
B = pow(g, b, p)

# Shared key
shared_alice = pow(B, a, p)
shared_bob = pow(A, b, p)

assert shared_alice == shared_bob

print("Alice public:", A)
print("Bob public:", B)
print("Shared key:", shared_alice)

# Real-Life Application explanation
explanation = '''
Diffie-Hellman (DH) is widely used in secure communication protocols such as the TLS handshake and Signal protocol.
It enables two parties to establish a shared secret over an insecure channel without transmitting the secret itself.
DH is crucial for ensuring forward secrecy, meaning even if keys are compromised later, past communication remains protected.
'''
with open("dh_usage.txt", "w") as f:
    f.write(explanation.strip())
