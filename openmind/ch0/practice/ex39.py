# -*- coding: utf-8 -*-
# create a mapping o f state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	}
	
# create a basic set of status and sone cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
	}
	
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# print some status
print '_' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Floridas's abbreviation is: ", states['Florida']

# do it by using the status then cities dict
print '_' *10
print "Michaigan has: ", cities[states['Michigan']]
print "Florida has: " ,cities[states['Florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state, abbrev)
	
#print every city in state
print '_' *10
for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev,city)
	
#now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(
		state,abbrev,cities[abbrev])
		
print '_' *10
# safely get a abbreviation by state that might not be there
state = states.get('Texas',False)

if not state:
	print "Sorry,no Texas."
	
# get a city with a default value
city = cities.get('TX','Does Not Exists')
print "The city for the state 'TX' is : %s" %city

mylove = {'apple':'big','orange':'soft','banana':'sweet'}
mylove['watermalon'] = 'watery'
print "I love the frite: ",mylove['watermalon']
print mylove.items() # 取出字典里的所有元素
print mylove.get('applle',4) # 取出字典里某个元素，没有显示后面的值
for a,b in mylove.items():  #for 循环取出所有知道
	print " I like %s is %s" %(a,b)
	
print mylove.keys()
print mylove.values()
mylove.update(cities)
print mylove
print mylove.popitem()
print cmp(states,cities)
