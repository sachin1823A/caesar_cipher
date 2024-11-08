def caesar_cipher(text, shift, option):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_value = 65 if char.isupper() else 97
            if option == "encrypt":
                result += chr((ord(char) - ascii_value + shift) % 26 + ascii_value)
            elif option == "decrypt":
                result += chr((ord(char) - ascii_value - shift) % 26 + ascii_value)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose(1/2/3): ")

        if choice == "1":
            text = input("Enter a message to Encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_text = caesar_cipher(text, shift, "encrypt")
            print("Encrypted text:", encrypted_text)
            print("")
        elif choice == "2":
            text = input("Enter a message to Decrypt: ")
            shift = int(input("Shift value: "))
            decrypted_text = caesar_cipher(text, shift, "decrypt")
            print("Decrypted text:", decrypted_text)
            print("")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again!")
            print("")
main()