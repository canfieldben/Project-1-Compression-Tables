"""
This is the main file to operate everything. Make sure you have entered you appropriate text into your text and binary input files
"""
from time import *

end_loop = True
while end_loop:
    decider = input("Would you like to convert into text or binary? (t/b)\nTo exit type \"e\"")
    if decider == 'e':
        break
    elif decider == "t":
        import convert_to_text
        print("Working... program will now exit... check text_output.txt")
        sleep(6)
        break
    elif decider == "b":
        import convert_to_binary
        print("working... program will now exit... check binary_output.txt")
        sleep(6)
        break
    else:
        print('please enter either \"t\" or \"b\"')
