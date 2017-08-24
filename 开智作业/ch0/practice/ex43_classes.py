# -*- coding: utf-8 -*-
class Scence(object):
	def __init__(self,next_step):
		self.next_step = raw_input('please decide whether forword or backword> ')
		if self.next_step =="forword":
			def enter(self):
				print "clas good"
			
#				if Central Corridor:
#				elif Laser Weapon Arimory:
#				elif The Bridge:
#				elif Escape Pod:
#				else Death:
		else:
			Death('Central_Corridor')
			
class Engine (object):
	
	def __init__(self,scene_map):
		
		self.scene_map = scene_map
		print self.scene_map
		
				
	def play (self):
		if self.scene_map == "Central_Corridor":
			Map(self.scene_map).opening_scene() #调用Map的object的opening_scene函数，注意参数的传递路径
			CentralCorridor(self.scene_map).enter()
		elif self.scene_map == "Laser_Weapon_Armory":
			Map(self.scene_map).opening_scene
			LaserWeaponArmory(self.scene_map).enter()
		elif self.scene_map =="The_Bridge":
			Map(self.scene_map).opening_scene()
			TheBridge(self.scene_map).enter()
		elif self.scene_map=="Escape_Pod":
			Map(self.scene_map).opening_scene()
			EscapePod(self.scene_map).enter()
		else:
			print "Sorry ,you become a dead man"
			
class Death(Scence):
	
	def enter(self,deadplace):
		self.deadplace = deadplace
		print" Sorry,you become a dead man"
		self.recover = raw_input('> Do you want to play again,choice yes or no')
		if self.recover == yes:
			Engine(self.deadplace).play #回到死亡时的地方
			
		else:
			print" GAME OVER!"
			exit(0)
			
class CentralCorridor(Scence):

	def enter(self):
		
		self.next_step = raw_input('please decide whether forword or backword: ')
		if self.next_step =="forword":

				YourAnswer = raw_input('What I really hate is :money or beauty:')
				if "money" == YourAnswer:
					print " Congratulations! You have overcome the Goshman."
					print "Now you can enter the next palace"
					a_map = Map(Map('Central_Corridor').next_scene()) #将下一个场景给赋值a_map
					a_game = Engine(a_map.name())
					a_game.play()
				else:
					Death('Central_Corridor')

class LaserWeaponArmory(Scence):
	def enter(self):
		
		self.next_step = raw_input('please decide whether forword or backword: ')
		if self.next_step =="forword":
			
				YourAnswer = raw_input('What I really hate is :you or me: ')
				if "you" == YourAnswer:
					print " Congratulations! You have overcome the Goshman."
					print "Now you can enter the next palace"
					a_map = Map(Map('Laser_Weapon_Armory').next_scene())
					a_game = Engine(a_map.name())
					a_game.play()
				else:
					Death('Laser_Weapon_Armory')
					
class TheBridge(Scence):
	def enter(self):
		
		self.next_step = raw_input('please decide whether forword or backword: ')
		if self.next_step =="forword":
			
				YourAnswer = raw_input('What I really hate is :key or box: ')
				if "key" == YourAnswer:
					print " Congratulations! You have overcome the Goshman."
					print "Now you can enter the next palace"
					a_map = Map(Map('The_Bridge').next_scene())
					a_game = Engine(a_map.name())
					a_game.play()
				else:
					Death('The_Bridge')
					
class EscapePod(Scence):
	def enter(self):
		
		self.next_step = raw_input('please decide whether forword or backword ')
		if self.next_step =="forword":
			
				YourAnswer = raw_input('What I really hate is :stress or ability ')
				if "stress" == YourAnswer:
					print " Congratulations! You have overcome the Goshman."
					print "Now you can go home now ,you will be  a hero in your planet"
					exit(0)
				else:
					Death('Escape_Pod')

class Map(object):


	def __init__(self,start_scene):
		self.start_scene = start_scene
		
	def name(self):
		return self.start_scene
		
	def next_scene(self):
		if self.start_scene == "Central_Corridor":
			self.scene_name = "Laser_Weapon_Armory"
		elif self.start_scene == "Laser_Weapon_Armory":
			self.scene_name ="The_Bridge"
		elif self.start_scene == "The_Bridge":
			self.scene_name ="Escape_Pod"
		else:
			print"Yes,Something is wrong again"
			self.scene_name ="The_Bridge"
#		elif self.start_scene == "Escape_Pod":
#			pass
		return self.scene_name
			
		
		
	def opening_scene(self):
		if self.start_scene == "Central_Corridor":
			print "Welcome To Central Corridor" ,
			print "You should go ahead to  Laser Weapon Arimory"
		elif self.start_scene == "Laser_Weapon_Armory":
			print "Welcome To Laser Weapon Arimory" ,
			print "You should go ahead to  The Bridge"
		elif self.start_scene == "The_Bridge":
			print "Welcome To The Bridge" ,
			print "You should go ahead to  Escape Pod"
		elif self.start_scene == "Escape_Pod":
			print "Welcome To Escape Pod" ,
			print "You should run run run leave here now"
		else :
			print "Something wrong happened."
a_map = Map('Central_Corridor')
a_game = Engine(a_map.name())
a_game.play()




				
		
		
			
	



		
			