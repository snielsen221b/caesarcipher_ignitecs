# What is a caesar cipher?

# ASCII/numbers for letters
# >>> char(65)
# 'A'
# >>> ord('A')
# 65

MAX_KEY_SIZE = 26


def get_mode():
    '''this function figures our if you'''


def get_key():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
