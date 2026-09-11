# ==========================================
#        CAESAR CIPHER PROJECT
# ==========================================

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def brute_force(text):
    print("\n========== BRUTE FORCE RESULTS ==========")

    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")


def main():

    while True:

        print("\n========================================")
        print("          CAESAR CIPHER TOOL")
        print("========================================")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Brute Force")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        # ---------------- ENCRYPT ----------------
        if choice == "1":

            text = input("\nEnter message: ")

            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("❌ Shift must be a number.")
                continue

            encrypted = caesar_encrypt(text, shift)

            print("\nOriginal Message :", text)
            print("Shift Value      :", shift)
            print("Encrypted Message:", encrypted)

        # ---------------- DECRYPT ----------------
        elif choice == "2":

            text = input("\nEnter encrypted message: ")

            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("❌ Shift must be a number.")
                continue

            decrypted = caesar_decrypt(text, shift)

            print("\nEncrypted Message:", text)
            print("Shift Value      :", shift)
            print("Decrypted Message:", decrypted)

        # ---------------- BRUTE FORCE ----------------
        elif choice == "3":

            text = input("\nEnter encrypted message: ")

            brute_force(text)

        # ---------------- EXIT ----------------
        elif choice == "4":

            print("\nThank you for using Caesar Cipher Tool!")
            break

        else:
            print("❌ Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
