# -*- coding: utf-8 -*-
class Parent(object):

	def override(self): #写函数的时候里面的self参数容易丢
		print "PARENT override()"
		
	def implicit(self): #此函数，子类没有，但子继承了就可以用
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent): #继承父类

	def override(self): # 覆盖父类的相同函数，这样子调用的时候，用的是子自己的函数
		print "CHILD override()"
		
	def altered(self):
		print "CHILD,BEFORE altered()"
		super(Child,self).altered() #在子将父函数覆盖后，super用法类似先找到子的父类，然后在用父类的函数，容易丢self
		print"CHILD,AFTER altered()"
		
dad = Parent()
son = Child()

dad.override()
son.override()

dad.implicit()
son.implicit() #子调用父的函数，展示的是父函数的功能

dad.altered()
son.altered()