from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next :
		how_much = int(next)
	else:
		dead ("Man, learn to tyoe a mumber.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		weird_room()
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to nove the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chew you leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else :
			print "I got no idea what that means."
			
			
def weird_room():
	print " Because you have take too much gold."
	print " We must test you wether have qualification own the wealth."
	print " Now if you do,the wealth belong you ,if not you belong here forever,no quit!"
	next = raw_input("who are you?")
	if "WUHU" ==next :
		print " The money belong you ,my lord!"
		exit(100)
	elif "Your master is all" ==next:
		print " yeah , my lord I have waited for you for 1000 years."
		print " Behind the wall ,there are more gold."
		print " Please take!"
		exit (0) #exit procedure
	else:
		print "Thank you for stay with me ,you and gold all are belonging here."
		dead("You are living the weird house for lives")
		
				
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you fiee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		

def dead(why):
	print why,"Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room ()
	elif next == "right":
		cthulhu_room
	else:
		dead("You stumble around the room until you starve.")
		
		
start()
