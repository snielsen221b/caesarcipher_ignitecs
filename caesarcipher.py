# https://inventwithpython.com/chapter14.html

# What is a caesar cipher?

# ASCII/numbers for letters
# >>> char(65)
# 'A'
# >>> ord('A')
# 65

MAX_KEY_SIZE = 26


def get_mode():
    '''this function figures our if your code
    is encrypting and decrypting'''
    # this is a while loop, it runs all the time if the condition is true
    # the while tells you the type of loop, the True is your condition
    # everything indented unded the while True: is in the loop
    while True:
        print("Do you wish to encrypt or dycrypt a message?")
        # input() sets the variable mode equal to what you type
        # .lower() puts mode in all lowercase
        mode = input().lower()

        # this line checks if the user input is valid (either encrypt or decrypt)
        # if it is, this function returns the mode
        if mode == 'encrypt' or mode == 'decrypt':
            return mode
        # if the input isn't encrypt or decrypt, the function displays the message
        else:
            print('Enter either "encrypt" or "decrypt"')


def get_message():
    '''This function asks the user for a message to
    be encrypted or decrypted'''
    # First we prompt the user for their message
    print('Enter your message:')
    # Return the message the user inputted to be used later in the code
    return input()


def get_key():
    '''This function defines the key for your Caesar Cipher.
    In other words, this will tell you by how many letters
    to shift the alphabet in your translated message'''
    key = 0
    while True:
        # Ask the user how many letters they weant to shift the key by
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        # Returning exits the infinite while loop and spits back the inputted
        # key value. Only return if the user entered a valid key
        # (in range of the alphabet)
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def get_translated_message(mode, message, key):
    if mode == 'decrypt':
        key = -key
    translated = ''

    for symbol in message:
        # Use isalpha to make sure each character in the message is an
        # uppercase or lowercase letter from a to z
        if symbol.isalpha():
            # use ord to get the number value associated with the letter
            num = ord(symbol)
            # add the value of key to the number
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated
