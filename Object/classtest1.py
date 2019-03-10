#!/usr/bin/env
#coding: utf-8


class UserData:
	def __init__(self,ID,name):
		self.ID = ID
		self.name = name
	
	def __repr__(self):
		return 'ID:{} Name:{}'.format(self.ID,self.name)

if __name__ == '__main__':
	user1 = UserData(101, 'Jack')
	user2 = UserData(102, 'Louplus')
	print(user1)
	print(user2)






