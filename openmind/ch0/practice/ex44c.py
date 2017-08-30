class Parent(object):
	
	def altered(self):
		print " PARENT altered()"
		
class Child (Parent):

	def altered(self):
		print "CHILFD, BEFORE PARENT altered()"
		super(Child,self).altered()
		print "CHILD, AFETER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()