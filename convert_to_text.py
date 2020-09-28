"""
converts binary to text
"""

import dictionary
from read_file import *


def text_assign(bin_dict, input_bin):
    split_list = []
    empty_str = " "
    for i in range(0, len(input_bin), 2):
        split_list.append(input_bin[i:i + 2])
    for r in split_list:
        if int(r) in dictionary.text_dictionary:
            empty_str += r + ":" + str(bin_dict[int(r)])
            print(r + ":" + str(bin_dict[int(r)]))
    return empty_str


trans_str = text_assign(dictionary.text_dictionary, binary_read_file())
binary_write_file(trans_str)
