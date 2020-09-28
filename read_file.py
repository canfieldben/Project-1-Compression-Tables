"""
Takes text document and stores content as a string
"""
import os


def text_read_file():
    input_string = open("text_input.txt", "r")
    input_transfer = input_string.read()
    input_string.close()
    return input_transfer


def text_write_file(new_text):
    output_string = open('text_output.txt', "w")
    output_string.write(new_text)
    output_string.close()


def binary_read_file():
    input_string = open("binary_input.txt", "r")
    input_transfer = input_string.read()
    input_string.close()
    return input_transfer


def binary_write_file(new_text):
    output_string = open("binary_output.txt", "w")
    output_string.write(new_text)
    output_string.close()
