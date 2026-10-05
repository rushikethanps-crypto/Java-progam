p = 23
g = 5

private_a = 6
private_b = 15

public_a = pow(g, private_a, p)
public_b = pow(g, private_b, p)

shared_key_a = pow(public_b, private_a, p)
shared_key_b = pow(public_a, private_b, p)

print("Alice Public Key:", public_a)
print("Bob Public Key:", public_b)
print("Alice Shared Key:", shared_key_a)
print("Bob Shared Key:", shared_key_b)