#!/usr/bin/env python3

#filename = input('Enter file path:')
#try:
#    f = open(filename)
#    print(f.read())
#    f.close()
#except FileNotFoundError:
#    print("File not found")

filename = '/etc/protocols'
f = open(filename)
#f.write('shiyanlou')
try:
    f.write('shiyanlou')
except :
#    raise FileWriteError()
    print('File write error')
finally:
    print('finally')
    f.close()

