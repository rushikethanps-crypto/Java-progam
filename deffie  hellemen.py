p = 9
q = 7

n = p * q
phi = (p - 1) * (q - 1)

e = 2
d = 29

message = 6

encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)

print("Message:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)