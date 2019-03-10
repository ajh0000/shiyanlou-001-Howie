#!usr/bin/env python3
#coding: utf-8

class Dog:
	def __init__(self,name,age): #创建类的实例时必须传入name参数
		self.name = name
		self.age = age

	def __repr__(self):
		return 'Dog: {}'.format(self.name)  #自定义打印格式


dog = Dog('旺财', 2) # 创建类的实例
print(dog)  #打印类的实例
print(dog.name)  #打印实例的属性 name
print(dog.age)

