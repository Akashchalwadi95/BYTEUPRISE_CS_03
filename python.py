def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine the shift direction based on the mode (encrypt or decrypt)
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
            result += shifted_char
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher tool!")
    while True:
        mode = input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ").lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            continue
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value (an integer between 1 and 25): "))
        if shift < 1 or shift > 25:
            print("Invalid shift value. Please enter an integer between 1 and 25.")
            continue
        if mode == 'encrypt':
            encrypted_text = caesar_cipher(text, shift, mode)
            print(f"Encrypted message: {encrypted_text}")
        elif mode == 'decrypt':
            decrypted_text = caesar_cipher(text, shift, mode)
            print(f"Decrypted message: {decrypted_text}")
        another = input("Do you want to encode/decode another message? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Caesar Cipher tool!")
            break

if __name__ == "__main__":
    main()
