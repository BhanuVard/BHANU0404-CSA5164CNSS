def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def affine_cipher(text, a, b, encrypt=True):
    result = ""
    a_inv = mod_inverse(a, 26) if not encrypt else 1
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            if encrypt:
                result += chr((a * (ord(char) - shift) + b) % 26 + shift)
            else:
                result += chr(a_inv * ((ord(char) - shift - b) % 26) % 26 + shift)
        else:
            result += char
    return result

# Example usage
plain_text = "HELLO WORLD"
a, b = 5, 8

encrypted = affine_cipher(plain_text, a, b, encrypt=True)
decrypted = affine_cipher(encrypted, a, b, encrypt=False)

print("Original:", plain_text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
