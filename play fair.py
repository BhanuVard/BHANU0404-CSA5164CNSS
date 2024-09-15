def create_matrix(key):
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and keep order
    matrix = [char for char in key if char.isalpha()]
    matrix = matrix + [char for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if char not in matrix]
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += 'X'
    return text

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character '{char}' not found in matrix")

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    text = preprocess_text(text)
    encrypted_text = ''
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        try:
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)
        except ValueError as e:
            print(e)
            continue
        
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
    
    return encrypted_text

key = input("Enter the key: ")
text = input("Enter the text to encrypt: ")
encrypted_text = playfair_encrypt(text, key)
print(f"Encrypted Text: {encrypted_text}")
