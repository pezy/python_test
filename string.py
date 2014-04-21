# -- coding: utf-8 --

name = 'Pezy'
age = 24 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'
nation = 'ÖÐ¹ú'
unsigned = -3

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
	age, height, weight, age + height + weight)

# really about me
print "I'm come from %s" % nation

# try some cool
print "%s %s %s" % (1, 2.3, ['one','two','three'])

# unsigned int?
print "%u" % unsigned

# float? easy
print "%f" % 3.1415926

# %e or %f , ok, how about %g?
print "%g" % 0.00000434
print "%g" % 3.141592658

# something like c language
print "%6.2f" % 1.2344

# something amaze
print "%(name)s:%(score)06.1f" % {'score':9.5, 'name':'pezy'}

# translate (must use quote) 
print "%.2f m" % (0.0254 * height)
print "%.2f kg" % (0.45359237 * weight)