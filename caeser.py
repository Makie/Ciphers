#!/usr/bin/env python3
""" Caeser Cipher.

http://inventwithpython.com/hacking/chapter6.html
"""

import utils
import string

MESSAGE = utils.file_in()
KEY = 13
MODE = "encrypt"
LETTERS = string.ascii_uppercase

def translate(message=MESSAGE, mode=MODE, key=KEY):
    message = message.upper()
    translated = ""

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "encrypt":
                num += key
            else:
                num -= key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol

    return translated

utils.file_out(translate())
