def add(a,b):
	print "ADDING %d + %d" %(a, b)
	return (a + b) /(a - b)

def subtract(a, b):
	print "SUBTRACTING %d -%d" % (a , b)
	return a - b/a

def multiply (a, b):
	print "MULTIPLY %d * %d " %(a, b)
	return a * b -10
	
def divide(a, b):
	print "DIVIDE %d / %d" %(a, b)
	return a / b +1
	
	
print "Let's do some math with just functions!"

age = add (30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
first_result = divide(iq, 2)
second_result = multiply(weight, first_result)
third_result = subtract(height, second_result)
last_result = add(age, third_result)

print "That becomes: ", last_result, "Can you do it by hand?"
