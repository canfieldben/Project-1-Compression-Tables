"""
Takes text document and stores content as a string
"""
import os
input_string = open("input.txt", "r")
input_print = input_string.read()
print(input_print)
input_string.close()

current_dir = os.getcwd()
