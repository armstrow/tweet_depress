'''
Changes format of feature files for use in Leo's pipeline. Input is text file in the format "<id>\t<text>" with one line per document, and a topic file in the format "<id>,<t1>,<t2>,...,<label>" where <t1> through <tn> are topic assignments for each document, and label is a symbolic label (+, -). Output is a single csv file in the format "<id>,<t1>,<t2>,...,<label>,<text>". 
'''


import sys

topic_file = open(sys.argv[1])
text_file = open(sys.argv[2])
out_file = open(sys.argv[3], "w")

text = {}
for line in text_file:
    try:
        vals = line.strip().split("\t")
        text[vals[0]] = vals[1]
    except:
        continue
text_file.close()

first = True
for line in topic_file:
    if first:
        first = False
        out_file.write("user" + line.replace("label", "avg") + ",text\n")
        continue
    docid = line.split(",")[0]
    out_file.write(line.strip().replace("+", "1").replace("-","0") + "," + text[docid] + "\n")
out_file.close()
