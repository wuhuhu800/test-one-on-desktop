# -*- coding: utf-8 -*-
from sys import argv #从系统调用argv 模块
scripts, filename = argv # 定义参数

txt = open(filename) # 执行open命令，将执行后的结果赋值给变量

print ("Here's your file %r:" % filename) #打印这段话，格式和字符
print (txt.read()) #文件调用read函数
txt.close()

print ("Type the filename again:") #打印这段话
file_again =input("> ") # 执行raw_input命令，将用户输入赋值给新变量

txt_again = open(file_again) # 执行open命令，将执行后的结果赋值给新的变量

print (txt_again.read()) # 文件调用read函数，并且打印出来
#print txt_again.next()
#print txt_again.next()

#print txt_again.tell()

txt_again.close()
