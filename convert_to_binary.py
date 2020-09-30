"""
Converts the string input to binary
"""

from read_file import *
import dictionary


def binary_assign(bin_dict, input_str):
    new_string = input_str.replace("and", "1").replace("the", "2").replace("of", "3").replace("th", "4").replace("er", "5").replace("on", "6").replace("an", "7").replace("ss", "8").replace("tt", "9").replace("ff", "$").replace("ea", "@").replace("he", "#").replace("in", "%").replace("\n", "&")
    #print(new_string)
    empty_str = ""
    for char in new_string:
        if char in bin_dict:
            empty_str += str(bin_dict[char])
            #print(char + ":" + str(bin_dict[char]))
    total = len(empty_str)
    empty_str = (str(total) + "." + empty_str)
    #print(empty_str)
    return empty_str


trans_str = binary_assign(dictionary.binary_dictionary, text_read_file())
text_write_file(trans_str)
