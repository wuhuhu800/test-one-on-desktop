# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #将变量分为元素，放入stuff变量的列表里
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10: #stuff 元素不等于10个
	next_one = more_stuff.pop() #将最后一个元素给next_one变量
	print "Adding: ", next_one #将next_one 变量打印
	stuff.append(next_one) #为stuff 和 next_one 调用 append 函数，将next_one 加入stuff列表里
	print "There's %d items now." %len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #打印第1个元素，不是第0个
print stuff[-1] #whoa! fancy
print stuff.pop() 
print stuff.pop() # 打印出最后一个元素，打印完之后不再显示
print ' '.join(stuff) #what? cool! 所以有元素之间增加空格.注意，‘’之间可以加很多元素例如\n \t
print '#'.join(stuff[3:6]) #super stellar! 列表第三个之后到第六个元素之间增加#