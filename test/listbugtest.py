#!/usr/bin/env python3

def compute(value, *base):
    if base == None:
        print("please input base")
    else:    
        base = list(base)
    base.append(value)
    result = sum(base)
    print(result)
    base = None

if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(15, *testlist)
    compute(25,*testlist)
    compute(35,*testlist)









