def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Parameters
prime_modulus = 23
generator = 5
alice_secret = 6
bob_secret = 15

# Compute public keys
alice_public = power_mod(generator, alice_secret, prime_modulus)
bob_public = power_mod(generator, bob_secret, prime_modulus)

# Compute shared secrets
shared_secret_alice = power_mod(bob_public, alice_secret, prime_modulus)
shared_secret_bob = power_mod(alice_public, bob_secret, prime_modulus)

# Output results
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)
print("Shared secret key (Alice):", shared_secret_alice)
print("Shared secret key (Bob):", shared_secret_bob)
