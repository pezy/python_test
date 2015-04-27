# import argv
from sys import argv
# set argv0 as filename
script, filename = argv
# open the file
txt = open(filename)
# print filename
print "Here's your file %r:" % filename
# print file content
print txt.read()
# input filename again
print "Type the filename again:"
# close the file
txt.close()
# get the filename again
file_again = raw_input("> ")
# open the file again
txt_again = open(file_again)
# print file content again
print txt_again.read()
# close the file 
txt_again.close()
