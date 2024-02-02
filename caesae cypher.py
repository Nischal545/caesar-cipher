def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    valid_modes = ['e', 'd']
    mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
    while mode not in valid_modes:
        print("Invalid Mode")
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()

    message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt"))
    shift = input("What is the shift number: ")
    while not shift.isdigit():
        print("Invalid Shift")
        shift = input("What is the shift number: ")

    return mode, message.upper(), int(shift)

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text



def main():
    welcome()
    while True:
        mode, message, shift = enter_message()
        if mode == 'e':
            encrypted_message = encrypt(message, shift)
            print("Encrypted message: {}".format(encrypted_message))
        else:
            decrypted_message = decrypt(message, shift)
            print("Decrypted message: {}".format(decrypted_message))

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        while another_message != 'y' and another_message != 'n':
            another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message == 'n':
            print("Thanks for using the program, goodbye!")
            break


if __name__ == '__main__':
    main()



























