"""
Converts the string input to binary
"""

from read_file import *
import dictionary


def binary_assign(bin_dict, input_str):
    empty_str = ""
    new_strings = []

    split_string = input_str.split()
    final_str = ""

    for string in split_string:
        new_string = string.replace("and", "1").replace("the", "2").replace("of", "3").replace("th", "4").replace("er", "5").replace("on", "6").replace("ss", "7").replace("tt", "8")
        new_strings.append(new_string)

    print(new_strings)
    for i in new_strings:
        final_str += " " + i
    print(final_str)

    for char in final_str:
        if char in bin_dict:
            empty_str += str(bin_dict[char])
            print(char + ":" + str(bin_dict[char]))
    total = len(empty_str)
    empty_str = (str(total) + "." + empty_str)
    return empty_str


trans_str = binary_assign(dictionary.binary_dictionary, text_read_file())
text_write_file(trans_str)
