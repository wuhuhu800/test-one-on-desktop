class Animal (object):
	def __init__ (self,other):
		self.other = other
		print self.other
		
	def show (self):
		for line in self.other:
			print line
		
	def like (self):
		self.mi = range(0,8)
		return self.mi
#	return self.other
			
myAnimal = Animal(["There are alot of anmimals",
					"every one has there lifes",
					"I love life in here"])
				
myAnimal.show()


class Person(object):
	def __init__(self,doing):
		self.doing = doing
		
	def yourName (self):
		games = self.doing.values()
		print games
		
myPerson = Person({"zhangsan":"football","lisi":"basketball","wangwu":"volleyball"})

myPerson.yourName()


class Fish(object):
	def __init__(self,fishes):
		self.fishes = fishes
		
	def EatFish(self):
		j = 1
		for i in self.fishes:
			print " this is %d kind fish to eat ,that is %s" %(j,i)
			j += 1
			
myFish = Fish(["hongshao Fish","qingzhen Fish","jian Fish","meng Fish"])

myFish.EatFish()

"""
Mi = range(0,7)
class Bike(object):
	def __init__(self,tool):
		self.tool = tool
	def play(self):
		for newLine in self.tool:
			print newLine
			
a_bike = Bike(myAnimal)
a_bike.play()

"""
	
		

