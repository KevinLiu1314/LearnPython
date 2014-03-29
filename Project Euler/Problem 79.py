# -*- coding: utf-8 -*-
# Problem 79
# Passcode derivation

# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown length.

# 1. This can be solve easily by import the text file into Excel, remove
# 2. duplicated entries, sort it first, then just manually figuring the code.

from time import time

start_time = time()

print "Answer:", 73162890

print "Total Time: ", time() - start_time

# Completed on Sat, 29 Mar 2014, 01:06
# Solve by: 24456
# ---------------
# Answer: 73162890
