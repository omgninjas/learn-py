#python 2
print "How old are you?",
##python 3
#age = int(input())
age = raw_input()
print "How tall are you?",
##python 3
#height = input()
height = raw_input()
print "How much do you weigh?",
##python 3
#weight = input()
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)