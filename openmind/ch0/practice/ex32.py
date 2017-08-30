# -*- coding: utf-8 -*-
the_count =[1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change =[1, 'pennies', 2, 'dimes', 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits: #遍历列表
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change :
	print "I got %r" %i
	
# we can also build list, first start with an empty one
# elements = []
elements = range(0,6) #直接给的是字符串格式的元素
elements[3:3] = ['insert'] #0：3直接将前三个覆盖；3：3将插入第三个之后
lenght=len (elements) #len() 查询列表有几个元素
print "this elements has %d elements" %lenght

# then use the range function to do 0 to 5 counts
#for i in range(0, 6):
	#print "Adding %d to the list." %i
	# append is a function that lists understand
	#elements.append(i) #往列表尾部里增加元素
	
# now we can print them  out too
for i in elements:  #遍历列表
	print"Element was: %r" %i


first = elements[0]
second = elements[1]
third = elements[2]
forth = elements[-1] # 倒数第一
fifth = elements[-2] #倒数第二
sixth =elements[-3] 


print first, second, third, forth, fifth, sixth

