def cheese_and_crackers(cheese_count,boxes_of_crackers): #自定义函数
 print "You have %d cheeses!" %cheese_count # 打印输出，输出用到函数第一参数值
 print "You have %d boxes of crackers!" %boxes_of_crackers #打印输出，输出用到函数第二参数值
 print "Man that's enough for a party!"
 print "Get a blancket.\n" #打印输出，并且回车
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) #将数字传给函数，使用函数


print "Or, we can use variables from our script:"
amount_of_cheese = 10 #将数字赋值给变量
amount_of_crackers = 50 #将数字赋值给变量

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #给函数传变量，调函数


print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6) #给函数传数字运算，run函数


print "And we can combine the two, variables and math:" #打印提示
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #给函数传参数，参数为变量与数字的运算
