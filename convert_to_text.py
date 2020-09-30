"""
converts binary to text
"""

import dictionary
from read_file import *


def text_assign(bin_dict, input_bin):
    split_list = []
    empty_str = ""
    index = 0
    while index < len(input_bin):
        first_num = input_bin[0]
        if first_num == '1':
            temp_str = input_bin[:5]
            split_list.append(temp_str)
            input_bin = input_bin[5:]
        if first_num == '0':
            temp_str = input_bin[:7]
            split_list.append(temp_str)
            input_bin = input_bin[7:]
    index += 1
    for i in split_list:
        if i in bin_dict:
            empty_str += str(bin_dict[i])
            #print(i + ":" + str(bin_dict[i]))
    #print(empty_str)
    return empty_str


trans_str = text_assign(dictionary.text_dictionary, binary_read_file())
binary_write_file(trans_str)
