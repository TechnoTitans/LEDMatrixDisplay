def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

f = open("signContent.txt", "r")

for line in f.readlines():
    print line
    v = line.split(",")
    print v
    whatisthis(v[0])
    if v[0] == "file":
        print "display file"

f.close()
