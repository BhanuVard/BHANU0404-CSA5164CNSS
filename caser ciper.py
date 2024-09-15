def caesar_cipher(msg, key, enc): 
    return ''.join(chr((ord(c) - (65 if c.isupper() else 97) + (key if enc else -key)) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in msg)

msg = input("Enter message: ")
key = int(input("Enter key (1-25): "))
if 1 <= key <= 25:
    enc = int(input("1. Encrypt\n2. Decrypt\nChoice: ")) == 1
    print("Result:", caesar_cipher(msg, key, enc))
else:
    print("Invalid key!")
