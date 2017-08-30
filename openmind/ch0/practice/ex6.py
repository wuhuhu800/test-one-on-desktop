# -*- coding: utf-8 -*-
x = "There are %d types of people ." % 10 #字符串赋值变量，用到格式化字符
binary = "binary" # 字符串赋值变量
do_not = "don't" # 字符串赋值变量
y = "Those who know %s and those who %s." % (binary,do_not) #字符串赋值变量，多格式化字符

print x #打印变量
print y #打印变量

print "I said: %r." % x # 打印字符串，格式化字符，将变量全部打印出
print "I also said: '%s'." % y # 打印字符串，格式化字符，将变量打印出

hilariois = False # 定义变量
joke_evaluation = "Isn't that joke so funny?! %r" # 定义变量

print joke_evaluation %hilariois # 打印变量，格式字符

w = "This is the left side of..." #字符串赋值变量
e = " a string with a right side." #字符串赋值变量

print w + e #打印变量组合


