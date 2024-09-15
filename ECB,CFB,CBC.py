from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    padding_len = 16 - len(data) % 16
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    return data[:-data[-1]]

def ecb_encrypt_decrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message))
    decrypted_message = unpad(cipher.decrypt(ciphertext))
    return ciphertext, decrypted_message

def cbc_encrypt_decrypt(message, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message))
    decrypted_message = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext))
    return ciphertext, decrypted_message, iv

def cfb_encrypt_decrypt(message, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(message)
    decrypted_message = AES.new(key, AES.MODE_CFB, iv).decrypt(ciphertext)
    return ciphertext, decrypted_message, iv

message = b"Hello, AES Modes!"
key = get_random_bytes(16)

# ECB Mode
ecb_ciphertext, ecb_decrypted = ecb_encrypt_decrypt(message, key)
print("\nECB Mode:")
print("Ciphertext:", ecb_ciphertext)
print("Decrypted:", ecb_decrypted)

# CBC Mode
cbc_ciphertext, cbc_decrypted, cbc_iv = cbc_encrypt_decrypt(message, key)
print("\nCBC Mode:")
print("Ciphertext:", cbc_ciphertext)
print("Decrypted:", cbc_decrypted)

# CFB Mode
cfb_ciphertext, cfb_decrypted, cfb_iv = cfb_encrypt_decrypt(message, key)
print("\nCFB Mode:")
print("Ciphertext:", cfb_ciphertext)
print("Decrypted:", cfb_decrypted)
