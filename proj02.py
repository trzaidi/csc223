# Step 1: Input the cipher text directly
def get_cipher_text():
    # Replace this with the cipher text you want to decrypt
    cipher_text = "L FDQQRW ZDLW WR OHDYH QYFF"
    return cipher_text.replace(" ", "")  # Remove spaces for analysis

# Step 2: Count the occurrences of each letter
def count_letters(cipher_text):
    letter_counts = [0] * 26  # Create a list of 26 zeros, one for each letter
    for char in cipher_text:
        if char.isalpha():  # Only count alphabetic characters
            index = ord(char.upper()) - ord('A')  # Convert letter to index (A=0, B=1, ..., Z=25)
            letter_counts[index] += 1
    return letter_counts

# Step 3: Find the most common letter
def find_most_common_letter(letter_counts):
    max_count = max(letter_counts)  # Find the maximum count in the list
    most_common_index = letter_counts.index(max_count)  # Find the index of the most common letter
    return most_common_index

# Step 4: Determine the shift
def calculate_shift(most_common_index):
    # 'E' is at index 4 (since A=0, B=1, ..., E=4)
    expected_index = ord('E') - ord('A')
    shift = (most_common_index - expected_index) % 26
    return shift

# Step 5: Decrypt the cipher text using the calculated shift
def decrypt_message(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Convert the character to an index (A=0, B=1, ..., Z=25)
            index = ord(char.upper()) - ord('A')
            # Apply the reverse shift
            decrypted_index = (index - shift) % 26
            # Convert back to a letter
            decrypted_char = chr(decrypted_index + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Keep non-alphabetic characters as they are (spaces, etc.)
    return decrypted_text

# Step 6: Main function to run all steps
def main():
    cipher_text = get_cipher_text()
    letter_counts = count_letters(cipher_text)
    most_common_index = find_most_common_letter(letter_counts)
    shift = calculate_shift(most_common_index)
    decrypted_message = decrypt_message(cipher_text, shift)
    print("Decrypted Message:", decrypted_message)

# Run the main function
if __name__ == "__main__":
    main()