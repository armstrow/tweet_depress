import sys


f = open(sys.argv[1], "r")
o = open(sys.argv[2], "w")
l = open(sys.argv[3], 'r')

labels = {}
for line in l:
    vals = line.strip().split("\t")
    labels[vals[0]] = vals[1]
#print labels

first = True
lcount = 0
o.write("id," + ",".join([str(i) for i in range(0,50)]) + ",label\n")
for line in f:
    if first:
        first = False
        continue
    vals = line.strip().split(" ")
    count = 0
    topics = {}
    while count < len(vals):
        if count == 1:
            doc = vals[count].split("/")[-1]
        elif count > 1:
            topic = vals[count]
            topics[int(topic)]= float(vals[count + 1])
            count += 1
        count += 1    
    #print topics
    s = str(doc) + ","
    for i in range(0, 50):
        if i in topics:
            s += str(topics[i]) + ","
        else:
            s += "0,"
    if float(labels[doc]) == 1:
        s += "+"
    elif float(labels[doc]) == 0:
        s += "-"
    else:
        print "error", labels[doc]
        break
    #s += labels[lcount]
    print lcount
    lcount += 1
    o.write(s + "\n")
    
