# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read() #打印文件类型读到内容
	
def rewind(f):
	f.seek(0) #将文件内容的光标从第0个字母开始
	
def print_a_line(line_count, f): #自定义函数
	print line_count, f.readline(), #打印第一参数，打印读取的该行内容
	

	
current_file = open(input_file ) #将用户文件名转为文件类型赋值给变量

print "Frist let's print the whole file:\n"

print_all(current_file) #运行自定义函数
print current_file.tell()

print "Now let's rewind, kind of like a tape."

rewind(current_file) #运行自定义函数，从第X字母开始
print current_file.tell()

print "Let's print three lines:"

current_line =1 #变量赋值1 
print_a_line(current_line,current_file) #运行自定义函数


current_line = current_line + 1
print_a_line(current_line, current_file) 

#print current_file.tell()
#current_file.writelines("this is a pen.")

current_line = current_line + 1 # 变量+1
print_a_line(current_line,current_file) # 运行变量+1后的参数的函数，注意，readline函数每次运行完之后会停到那一行
print current_file.tell()
