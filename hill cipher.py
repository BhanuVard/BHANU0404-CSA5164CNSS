import numpy as np

def char_to_index(c):
    return ord(c.lower()) - ord('a')

def index_to_char(index):
    return chr(index + ord('a'))

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").lower()
    n = key_matrix.shape[0]
    ciphertext = ""
    
    # Ensure plaintext length is a multiple of key size
    while len(plaintext) % n != 0:
        plaintext += 'x'  # Padding with 'x' if necessary

    for i in range(0, len(plaintext), n):
        block = np.array([char_to_index(c) for c in plaintext[i:i + n]])
        block = block.reshape(-1, 1)  # Reshape to a column vector
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(index_to_char(int(c)) for c in encrypted_block.flatten())
    
    return ciphertext

def main():
    key_matrix = np.array([[18, 21], [21, 18]])
    plaintext = "hello"
    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"Encrypted ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
