
def text_assign(input_bin):
    print(f)
    split_list = []
    empty_str = " "
    for i in input_bin:
        print(input_bin)
        if i == '1':
            #print(i+"S")
            temp_str = input_bin[:5]
            split_list.append(temp_str)
            input_bin = input_bin[5:]
        if i == '0':
            #print(i+"L")
            temp_str = input_bin[:7]
            split_list.append(temp_str)
            input_bin = input_bin[7:]
    return split_list



f = "101010011100101110001111"
print(text_assign(f))
