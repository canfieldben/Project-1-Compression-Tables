"""
Takes text document and stores content as a string
"""
import os


input_string = open("input.txt", "r")
input_transfer = input_string.read()
input_string.close()


def write_file(new_text):
    output_string = open('output.txt', "w")
    output_string.write(new_text)
    output_string.close()


