def permute(input_val, table):
    result = 0
    size = len(table)
    for i in range(size):
        bit = (input_val >> (64 - table[i])) & 1
        result |= bit << (size - 1 - i)
    return result

def des_decrypt(ciphertext, key):
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    
    permuted_ciphertext = permute(ciphertext, IP)
    decrypted = permuted_ciphertext ^ key
    decrypted = permute(decrypted, IP_INV)
    
    return decrypted

# Constants
KEY = 0x133457799BBCDFF1
CIPHERTEXT = 0x0123456789ABCDEF

# Decrypt the ciphertext
decrypted = des_decrypt(CIPHERTEXT, KEY)

print(f"Ciphertext: 0x{CIPHERTEXT:016X}")
print(f"Decrypted: 0x{decrypted:016X}")
