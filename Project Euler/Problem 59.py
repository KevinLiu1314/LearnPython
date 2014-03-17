# -*- coding: utf-8 -*-
# Problem 59
# XOR decryption

# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key. The advantage
# with the XOR function is that using the same encryption key on the cipher
# text, restores the plain text; for example, 65 XOR 42 = 107, then
# 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.

from time import time
import string


def key():
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                yield [ord(i), ord(j), ord(k)]

start_time = time()

# 1. read in the encrypted message
# 2. for all the possible 3 letters combination "k":
# 3.    cyclically build a "decoder" that's at least as long as the encrypted message
# 4.    XOR the encrypted message with "decoder" and call it "message"
# 5.    convert "message" to a string "message_str"
# 6.    see how many times the "test_word" appears in "message_str"
# 7.    if the count is > 5, print the key "k" and the "message_str"
# 8.    and sum up "message" as the answer

encrypted_msg = map(int, open("problem 59.txt").read().split(","))

test_word = "the"
kengen = key()

for k in kengen:
    decoder = []
    while len(decoder) < len(encrypted_msg):    # maybe a little longer, but no problem
        decoder.extend(k)

    message = [encrypted_msg[i] ^ decoder[i] for i in range(len(encrypted_msg))]
    message_str = "".join(map(chr, message))
    if message_str.count(test_word) > 5:
        print map(chr, k), message_str
        print sum(message)
        break

print "Total Time: ", time() - start_time

# Completed on Tue, 11 Mar 2014, 00:56
# Solve by: 21290
# ---------------
# ['g', 'o', 'd'] 107359 (The Gospel of John, chapter 1) 1 In the beginning the Word already existed.
# 107359
# Total Time:  2.41499996185
# [Finished in 2.7s]
