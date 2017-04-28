from sys import argv

script, filename = argv
#makes something called a "file object." 
#You can think of a file like an old tape drive that you saw on mainframe computers in the 1950s, or even like a DVD player from today. 
#You can move around inside them, and then "read" them, but the DVD player is not the DVD the same way the file object is not the file's contents.
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
#changes the prompt
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()