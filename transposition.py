#!/usr/bin/env python3
""" Transposition Cipher.

http://inventwithpython.com/hacking/chapter8.html
"""

import utils


def main():
    """ Docstring for main. """
    myMessage = "Common sense is not so common."
    myKey = 8

    ciphertext = encrypt_message(myKey, myMessage)

    print("{}|".format(ciphertext))
    print(ciphertext == "Cenoonommstmme oo snnio. s s c")


def encrypt_message(key, message):
    """ Docstring for encrypt_message. """
    ciphertext = ["" for x in range(len(message))]

    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)


if __name__ == '__main__':
    main()