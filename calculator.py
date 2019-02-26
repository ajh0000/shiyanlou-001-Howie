#!/usr/bin/env python3
# _*_coding:utf-8_*_

import sys
print(sys.argv)
wage = sys.argv[1]

def save_int(values):
	try:
		value = int(values)
		print('wage is',value)
		return value
	except ValueError:
		print('Parameter Error')


def Taxes(wage):
	try:
		wage = int(wage)
		# print('wage is',wage)
	except ValueError as e:
		print('Parameter Error')
		return e

	Tax = wage -(0+3500)
	if Tax <= 0:
		Taxes = wage
	elif Tax <= 1500:
		Taxes = Tax*0.03
	elif Tax <=4500:
		Taxes = Tax*0.1 - 105
	elif Tax <= 9000:
		Taxes = Tax*0.2 - 555
	elif Tax <= 35000:
		Taxes = Tax*0.25 - 1005
	elif Tax <= 55000:
		Taxes = Tax*0.30 - 2755
	elif Tax <= 80000:
		Taxes = Tax*0.35 - 5505
	else:
		Taxes = Tax*0.45 - 13505

	return Taxes

if __name__ == '__main__':
	Taxes = Taxes(wage)
	print(format(Taxes,".2f"))