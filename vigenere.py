def vigenere_encrypt(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper().replace(' ', '')
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    encrypted_text = ''
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k) - ord('A')
            encrypted_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += p
    
    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    ciphertext = ciphertext.upper().replace(' ', '')
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    
    decrypted_text = ''
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k) - ord('A')
            decrypted_char = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += c
    
    return decrypted_text

key = input("Enter the key for Vigenère cipher: ")
text = input("Enter the text to encrypt: ")
encrypted_text = vigenere_encrypt(text, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
