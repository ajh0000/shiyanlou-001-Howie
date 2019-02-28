#! /usr/bin/env python3

import sys
list_input = sys.argv[1:]

list_B = []
list_L = []

# counts = len(list_input)
for i in range(len(list_input)):
    l_input = list_input[i]
    if len(l_input) > 3:
        list_B.append(l_input)
    else:
        list_L.append(l_input)

print(list_L)
print(list_B)




