# Given an integer, , print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print
# Prints
# The four values must be printed on a single line in the order specified above for each i from 1 to number. 
# Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

# Solution

def print_formatted(number):
    pad = number.bit_length()
    for i in range(1,number+1):
        print(str(i).rjust(pad),oct(i).split("o")[1].rjust(pad),hex(i).split("x")[1].upper().rjust(pad),bin(i).split("b")[1].rjust(pad))
