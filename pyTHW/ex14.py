from sys import argv

script, user_name = argv
'''
We make a variable prompt that is set to the prompt we want, and we give that to raw_input instead of typing it over and over. 
Now if we want to make the prompt something else, we just change it in this one spot and rerun the script.
'''
prompt = '$ '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)