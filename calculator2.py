#!/usr/bin/env python3
# _*_coding:utf-8_*_

import sys

class Pay_aclc():
        # """docstring for Pay_aclc"""
        # def __init__(self):
        #       args = sys.argv[1:]                     
        def save_input(self,args):
                # print(args)
                input_dict = {}
                for arg in args:
                        ID = arg.split(':')[0]
                        wage = arg.split(':')[1]
                        try:
                                wage = int(wage)
                                # print('wage is',wage)
                                input_dict[ID] = wage
                        except ValueError as e:
                                print('Parameter Error')
                                return e
                # print(input_dict)
                return input_dict       

                

        def Shebao(self,wage):
                # try:
                #       wage = int(wage)
                # except ValueError as e:
                #       print('Parameter Error')
                #       return e
                Shebao = wage *(0.08 + 0.02 + 0.005 + 0 + 0 + 0.06)
                return Shebao

        def Taxes(self,wage):
                Shebao = self.Shebao(wage)
                Tax = wage -(Shebao + 3500)
                if Tax <= 0:
                        Taxes = 0
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

        def output_Salary(self,args):
                input_dict = self.save_input(args)
                # output_Salary = {}
                for key,value in input_dict.items():
                        Taxes = self.Taxes(value)
                        # Taxe = Taxes(value)[0]
                        # Shebao = Taxes(value)[1]
                        Salary = value - Taxes[0] - Taxes[1]
                        # output_Salary[key] = Salary
                        print('{}:{:.2f}'.format(key, Salary))


if __name__ == '__main__':
        # Taxes = Taxes(wage)
        # print(format(Taxes,".2f"))
        calc = Pay_aclc()
        # input_dict = calc.save_input()
        calc.output_Salary(sys.argv[1:])
