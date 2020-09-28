"""
Converts the string input to binary
"""

import read_file
import dictionary


def binary_assign(bin_dict, input_string):
    for char in input_string:
        if char in bin_dict:
            print(char + ":" + str(bin_dict[char]))
    return


binary_assign(dictionary.binary_dictionary, read_file.input_transfer)
