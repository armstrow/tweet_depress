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
    vals = line.strip().split("\t")
    s = vals[1] + ',' + ",".join(vals[2:])
    '''
    count = 0
    topics = {}
    while count < len(vals):
        if count == 0:
            doc = int(vals[count])
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
    '''
    if float(labels[vals[1]]) == 1:
        s += ",+"
    elif float(labels[vals[1]]) == 0:
        s += ",-"
    else:
        print "error", labels[vals[1]]
        break
    #s += labels[lcount]
    print lcount
    lcount += 1
    o.write(s + "\n")
    
