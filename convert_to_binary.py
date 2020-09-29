"""
Converts the string input to binary
"""

from read_file import *
import dictionary


def binary_assign(bin_dict, input_str):
    empty_str = ""
    for char in input_str:
        if char in bin_dict:
            empty_str += str(bin_dict[char])
            print(char + ":" + str(bin_dict[char]))
    total = len(empty_str)
    empty_str = (str(total) + "." + empty_str)
    return empty_str


trans_str = binary_assign(dictionary.binary_dictionary, text_read_file())
text_write_file(trans_str)
