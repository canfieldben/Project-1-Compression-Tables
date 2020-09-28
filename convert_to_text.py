"""
converts binary to text
"""

import dictionary
from read_file import *


test_string = "1234678910"


def text_assign(bin_dict, input_bin):
    split_list = []
    empty_str = " "
    for i in range(0, len(test_string), 2):
        split_list.append(test_string[i:i + 2])
    for r in split_list:
        if int(r) in dictionary.text_dictionary:
            empty_str += r + ":" + str(bin_dict[int(r)])
            print(r + ":" + str(bin_dict[int(r)]))
    return empty_str


text_assign(dictionary.text_dictionary, test_string)
