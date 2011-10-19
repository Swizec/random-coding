
i = 5

for i in range(2):
    print "for:", i

print "after:", i


i = 5

for j in range(2):
    i = j+1
    print "for2:", i

print "after:", i

i = 5

print [i for i in range(2)]

print "after:", i
