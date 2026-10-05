from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

message = input("Enter message: ").encode()

ciphertext, tag = cipher.encrypt_and_digest(message)

print("Original:", message.decode())
print("Encrypted:", ciphertext.hex())
print("Key:", key.hex())