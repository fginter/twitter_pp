import sys
print "["
first=True
for line in sys.stdin:
    line=line.strip()
    if not line or line[0]!="{":
        continue
    if not first:
        print ","
    print line,
    first=False
print "]"


    
