from sys import argv

script, name, age, company = argv

print "The name of the script:", script
print "Your name:", name
print "Your age:", age
print "Your company:", company

workingAge = raw_input("Your working age is ?")

print "%r can know that: %r, your age is %r, and you have worked at %r more than %r years." % (script, name, age, company, workingAge)
