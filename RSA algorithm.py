from sympy import isprime, mod_inverse
import random

def generate_keypair(p, q):
    # Ensure p and q are prime
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime.")
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.choice([x for x in range(2, phi) if gcd(x, phi) == 1])
    # Compute d
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(message, public_key):
    e, n = public_key
    # Convert message to integers and encrypt
    return [pow(ord(char), e, n) for char in message]

def decrypt(encrypted_message, private_key):
    d, n = private_key
    # Decrypt integers back to characters
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)

# Example usage
p, q = 61, 53
public_key, private_key = generate_keypair(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

message = "HELLO"
print("Original Message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
