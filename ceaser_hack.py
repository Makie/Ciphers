#!/usr/bin/env python3
""" Caeser Cipher Hack.

http://inventwithpython.com/hacking/chapter7.html
"""

import utils
import caeser
import string

MESSAGE = utils.file_in()
LETTERS = string.ascii_uppercase


def force(message=MESSAGE):
    """ Brute force the passed message using the ceaser cipher. """
    for key in range(len(LETTERS)):
        translated = caeser.translate(message=message, mode="decrypt", key=key)
        print("Key {}: {}".format(key, translated))

force()
