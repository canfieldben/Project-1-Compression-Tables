"""
Converts the string input to binary
"""
# imports required functions
from read_file import *
import dictionary

# assigns the correct character to its binary assignment
def binary_assign(bin_dict, input_str):
    # replaces letter combo's with one letter combo to be assigned binary
    new_string = input_str.replace("and", "1").replace("the", "2").replace("of", "3").replace("th", "4").replace("er", "5").replace("on", "6").replace("an", "7").replace("ss", "8").replace("tt", "9").replace("ff", "$").replace("ea", "@").replace("he", "#").replace("in", "%").replace("\n", "&").replace("re", "^").replace("nt", "*")
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


# runs the function and then passes final string to be written in the text file
trans_str = binary_assign(dictionary.binary_dictionary, text_read_file())
text_write_file(trans_str)
