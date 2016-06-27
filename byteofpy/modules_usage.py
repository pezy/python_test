from sys import argv, path

print 'The command line arguments are'
for i in argv:
    print i

print '\n\nThe PYTHONPATH is', path, '\n'

from os import getcwd
print getcwd()

from math import sqrt
print 'Square root of 16 is', sqrt(16)

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'

import modules
modules.say_hi()
print 'Version', modules.__version__
