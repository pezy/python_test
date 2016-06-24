for i in range(1, 5):
    print i
else:
    print "loop is over."

while True:
    s = raw_input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Too small'
        continue
    print 'Input is sufficient length'
    print 'Length of the string is', len(s)
print 'Done'
