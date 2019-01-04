#!/usr/bin/env python3
# _*_coding:utf-8_*_

import sys

age = sys.argv[1]
age = int(age)
if age >= 0 and age < 10:
#if age not in [10,18) and [18,120):
    print('you belong to kids')
elif age >= 10 and age < 18:
    print('you belong to teenager')
elif age >= 18 and age < 30:
    print('you belong to adult')
elif age >= 30 and age < 60:
    print('you belong to older')
elif age >= 60 and age < 120:
    print('you belong to oldest')
