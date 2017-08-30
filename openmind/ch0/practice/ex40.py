# -*- coding: utf-8 -*-
class Song(object):

	def __init__(self, lyrics): #双下划线
		self.lyrics = lyrics # self.变量就是在该类里面全局的变量
		
		
	def sing_me_a_song(self):
		m = {'wuhu':'name','yunlin':'city'}
		for line in self.lyrics:
			print line
		print m['wuhu']	
happy_bday = Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there" ])
				
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
					
