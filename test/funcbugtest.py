#!/usr/bin/env python3


def compute(start,end):
    result = 0
    while start <= end:
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    start = 1
    end = 100
    compute(start,end)





