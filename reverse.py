""" Reverse Cipher

http://inventwithpython.com/hacking/chapter5.html
"""

import utils

message = utils.file_in()
output = ""

i = len(message) - 1

while i >= 0:
    output = output + message[i]
    i -= 1
    print(i, output)

print(output)