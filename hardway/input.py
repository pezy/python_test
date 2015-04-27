# raw_input : input anything will look as string

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

# other useage

# input to string
id = raw_input("input some text: ")

print "your text len is %r" % len(id)

# 0x
nHex = int(raw_input("input hex value(like 0x20): \n"), 16)

print "nHex = %x, nDec = %d\n" % (nHex, nHex)

# 0
nOct = int(raw_input("input orc value(like 020): \n"), 8)

print "nOrc = %o, nDec = %d\n" % (nOct, nOct)

# my own
name = raw_input("what is your name? ")
where = raw_input("where are you from? ")
aim = raw_input("what is your aim? ")

print "Hi, %r, %r is a great place, and %r will be better!" % (name, where, aim)
