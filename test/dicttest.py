#!/usr/bin/env python3

import sys

output_dict = {}
def handle_data(i):
    i_key = i.split(':')[0]
    i_value = i.split(':')[1]
    output_dict[i_key] = i_value

def print_data(x,y):
    print('ID:',x,'Name:',y)    


if __name__ == '__main__':
    
    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])


