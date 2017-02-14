# What is a caesar cipher?

# ASCII/numbers for letters
# >>> char(65)
# 'A'
# >>> ord('A')
# 65

max_key_size = 26


def get_mode():
    '''this function figures our if your code
    is encrypting and decrypting'''
    # this is a while loop, it runs all the time if the condition is true
    # the while tells you the type of loop, the True is your condition
    # everything indented unded the while True: is in the loop
    while True:
        print("Do you wish to encrypt or dycrypt a message?")
        mode = input().lower()
