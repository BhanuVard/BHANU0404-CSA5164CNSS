def rail_fence_encrypt(plaintext, rails):
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    direction = 1  # 1 means down, -1 means up
    row = 0
    
    for col in range(len(plaintext)):
        fence[row][col] = plaintext[col]
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction
    
    encrypted_text = ''.join(''.join(row).replace('', '') for row in fence)
    return encrypted_text

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = 1  # 1 means down, -1 means up
    row = 0
    
    # Mark the positions in the fence
    for col in range(len(ciphertext)):
        fence[row][col] = '*'
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction
    
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*':
                fence[r][c] = ciphertext[index]
                index += 1
    
    decrypted_text = ''
    row = 0
    direction = 1
    
    for col in range(len(ciphertext)):
        decrypted_text += fence[row][col]
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction
    
    return decrypted_text

rails = int(input("Enter the number of rails: "))
text = input("Enter the text to encrypt: ").replace(' ', '').upper()
encrypted_text = rail_fence_encrypt(text, rails)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print(f"Decrypted Text: {decrypted_text}")
