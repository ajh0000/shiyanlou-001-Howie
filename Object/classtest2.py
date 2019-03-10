#!/usr/bin/env
#coding: utf-8


class UserData:
	def __init__(self,ID,name):
		self.ID = ID
		self.name = name
	
	def __repr__(self):
		return 'ID:{} Name:{}'.format(self.ID,self.name)

class NewUser(UserData): #继承父类 UserData
	def __init__(self,ID,name):   
		UserData.__init__(self,ID,name) #继承父类的 __init__
		self.name = name
	def set_ID(self,ID):
		self.ID = ID
	def set_name(self,name):
		self.name = name




if __name__ == '__main__':
	user1 = NewUser(101, 'Jack')
	user1.set_name('Jackie')
	user2 = NewUser(102, 'Louplus')
	print(user1)
	print(user2)















