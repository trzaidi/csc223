def decrypt_cipher_with_known_shift(cipher_text, known_shift):
    decrypted_message = []
    for letter in cipher_text:
        if letter.isalpha():
            index = (ord(letter.lower()) - ord('a') - known_shift) % 26
            decrypted_letter = chr(index + ord('a'))
            decrypted_message.append(decrypted_letter)
        else:
            decrypted_message.append(letter)
    return ''.join(decrypted_message)

# Storing both the cipher text and the plain text
cipherText = "L fdqqrw zdlw wr ohdyh QYFF"
plainText = "I cannot wait to leave NVCC"

# Using known shift
shift = 3

# Perform decryption
decrypted_message = decrypt_cipher_with_known_shift(cipherText, shift)

# Output the decrypted message
print(f"Cipher text: {cipherText}")
print(f"Decrypted message: {decrypted_message}")
