"""
converts binary to text
"""
# imports required functions
import dictionary
from read_file import *


def text_assign(bin_dict, input_bin):
    split_list = [] # empty list
    empty_str = ""
    index = 0
    while index < len(input_bin): # loops through all of the numbers passed from the text file
        first_num = input_bin[0] # assigns the first number
        if first_num == '1': # if first number is "1" take the next 4 numbers and split
            temp_str = input_bin[:5]
            split_list.append(temp_str)
            input_bin = input_bin[5:]
        if first_num == '0': # if the first number is "0" take the next 6 numbers and split
            temp_str = input_bin[:7]
            split_list.append(temp_str)
            input_bin = input_bin[7:]
    index += 1
    for i in split_list: # assigns the binary numbers to assigned character
        if i in bin_dict:
            empty_str += str(bin_dict[i])
            #print(i + ":" + str(bin_dict[i]))
    #print(empty_str)
    return empty_str


# runs the function and passes it to be written in the output text file
trans_str = text_assign(dictionary.text_dictionary, binary_read_file())
binary_write_file(trans_str)
