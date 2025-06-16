def caesar_brute_force(ciphertext):
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   for shift in range(1, 26):
       result = ''
       for char in ciphertext:
           if char in alphabet:
               index = (alphabet.index(char) - shift) % 26
               result += alphabet[index]
           else:
               result += char
       print(f"{shift}: {result}")
#1
caesar_brute_force("Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu.")

#2
caesar_brute_force("mznxpz")

#3
import base64

def xor_decrypt(ciphertext_b64, key):
   ciphertext_bytes = base64.b64decode(ciphertext_b64)
   key_bytes = key.encode()
   decrypted = bytearray()

   for i in range(len(ciphertext_bytes)):
       decrypted_byte = ciphertext_bytes[i] ^ key_bytes[i % len(key_bytes)]
       decrypted.append(decrypted_byte)

   return decrypted.decode(errors='ignore')  # skip invalid characters

ciphertext = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
key = "secure"
plaintext = xor_decrypt(ciphertext, key)
print("Decrypted message:", plaintext)
