from sys import argv

script, user_name , gender = argv
jello = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd lke to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(jello)

print "where do you live %s?" % user_name
lives = raw_input(jello)

print "What kind of computer do you have?"
computer = raw_input(jello)

print "What gender do you like %s?" % gender
my_like = raw_input(jello)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Last but not least you said you like %s,right?
""" % (likes,lives,computer,my_like)
