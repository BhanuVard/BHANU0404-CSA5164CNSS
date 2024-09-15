from collections import Counter
import string

ALPHABET_SIZE = 26

def calculate_letter_frequency(text):
    text = text.lower()
    frequency = Counter(c for c in text if c in string.ascii_lowercase)
    return frequency

def decrypt_with_key(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            base_char = 'a' if char.islower() else 'A'
            index = ord(char.lower()) - ord('a')
            decrypted_char = chr((key[index] + ord(base_char)))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    return ''.join(plaintext)

def find_most_frequent_letter(frequency):
    max_char = max(frequency, key=frequency.get)
    return ord(max_char) - ord('a')

def letter_frequency_attack(ciphertext):
    frequency = calculate_letter_frequency(ciphertext)
    most_frequent_index = find_most_frequent_letter(frequency)
    shift = (most_frequent_index + ALPHABET_SIZE - (ord('e') - ord('a'))) % ALPHABET_SIZE
    key = [(i - shift + ALPHABET_SIZE) % ALPHABET_SIZE for i in range(ALPHABET_SIZE)]
    plaintext = decrypt_with_key(ciphertext, key)
    return plaintext

def main():
    ciphertext = "Gwc uivioml bw nqvl bpm zqopb apqnb"
    plaintext = letter_frequency_attack(ciphertext)
    print(f"Decrypted plaintext: {plaintext}")

if __name__ == "__main__":
    main()
