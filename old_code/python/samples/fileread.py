f = open("signContent.txt", "r")

x = "line"
y = "line"
if x == y:
    print 'match'

for line in f:
    v = line.strip().split(',')
    print v[0]
    if (line.startswith('file')):
        print "in the if"

f.close()
