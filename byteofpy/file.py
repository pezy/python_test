poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for writing
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
f.close()

# If no mode is specified
# Read mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    print line,
f.close()
