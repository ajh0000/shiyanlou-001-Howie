#! /usr/bin/env python3

import sys

dict_input = sys.argv[1:]

input_dict = {}

for i in range(len(dict_input)):
    temp_input = dict_input[i].split(':')
#    print(temp_input)
    input_dict[temp_input[0]] = temp_input[1]

for key,value in input_dict.items():
    print('ID:',key,'Name:',value)
     







