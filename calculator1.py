#!/usr/bin/env python3
# _*_coding:utf-8_*_

import sys
print(sys.argv)
args = sys.argv[1:]
# def input_dict(args):
input_dict = {}
for arg in args:
	ID = arg.split(':')[0]
	wage = arg.split(':')[1]
	input_dict[ID] = wage

def Shebao(wage):
	try:
		wage = int(wage)
	except ValueError, e:
		print('Parameter Error')
		return e
	Shebao = wage *(0.08 + 0.02 + 0.005 + 0 + 0 + 0.06)
	return Shebao

def Taxes(wage):
	try:
		wage = int(wage)
		# print('wage is',wage)
	except ValueError as e:
		print('Parameter Error')
		return e
	Shebao = Shebao(wage)
	Tax = wage -(Shebao + 3500)
	if Tax <= 0:
		Taxes = wage
	elif Tax <= 1500:
		Taxes = Tax*0.03
	elif Tax <= 4500:
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

	return Taxes,Shebao








if __name__ == '__main__':
	Taxes = Taxes(wage)
	print(format(Taxes,".2f"))