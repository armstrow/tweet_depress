'''
Converts topic files in the format output by code in segan which contains topics listed in the form "<id> <topic_index> <topic_value> <topic_index2> <topic_value2> ...", where topic distribution values are identified by a topic index in the space prior to it.  This assumes a 50-topic run and will produce a file in the format "<id>,<t1>,<t2>,...,<t50>,<label>" where t1 through t50 are the topic distribution values for the topic indexed by the column, and the label is the documents label from the label input file.

Usage: python topics_to_csv.py assignment_file out_file label_file
'''


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
    
