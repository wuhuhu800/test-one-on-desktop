# -*- coding: utf-8 -*-
import random   
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" # 将链接赋值给
WORDS = [] #创建列表

PHRASES = {
	"class %%%(%%%):":
	 	"Make a class named %%% that is-a %%%.",
	 "class %%%(object):\n\tdef __init__(self, ***)":
	 	"class %%% has-a __init__ that takes self and *** parameters.",
	 "class %%%(obeject):\n\tdef ***(self,@@@)":
	 	"class %%% has-a function named *** that takes self and @@@ parameters.",
	 "*** = %%%()":
	 	"Set *** to an instace of class %%%.",
	 "***.***(@@@)":
	 	"From *** get the *** function , and call it with parameters self ,@@@.",
	 "***.*** = '***'":
	 	"From *** get the *** attribute and set it to '***'."
 }
	 
# do they want to drill phrases first
PHRASES_FIRST = False #将变量赋值False
if len(sys.argv) == 2 and sys.argv[1] =="english":  #判断sys的argv变量个数是否等于2，以及第1个位置元素是否english
	PHRASES_FIRST =True
		
# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #打开网页的txt文件，调用readlines函数，逐行写入word里
	WORDS.append(word.strip())  #strip什么意思？？？
		
		
def convert(snippet,phrase): #创建函数，有两个参数
	class_names = [w.capitalize() for w in 
					random.sample(WORDS, snippet.count("%%%"))] # capitalize/sample和count函数？？？
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
		
	for i in range(0, snippet.count("@@@")): 
		param_count = random.randint(1,3) #randint 函数？？？
		param_names.append(', '.join(random.sample(WORDS,param_count)))
			
	for sentence in snippet, phrase:
		result =sentence[:]
			
		#fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1) #三个参数，replace函数
				
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
				
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@",word,1)
				
		results.append(result)
			
	return results
		
		
# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets) #shffle函数
		
		for snippet in snippets:
			phrase =PHRASES[snippet]
			question, answer = convert(snippet,phrase)
			if PHRASES_FIRST:
				question,answer = answer,question
				
			print question
			
			raw_input("> ")
			print"ANSWER: %s\n\n" % answer
except EOFError:
	print " \nBye"	 	
	 