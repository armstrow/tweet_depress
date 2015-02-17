import sys
import json

assign_file = open(sys.argv[1])
doc_file = open(sys.argv[2], "r")
out_dir = sys.argv[3]
tag = sys.argv[4]

docs = []
for line in doc_file:
    docs.append(line.strip().split("\t")[0])

count = 0
dc = 0
for line in assign_file:
    if count % 3 == 1:
        vals = line.strip().split("\t")
        topics = vals[52:]
        data = {}
        ti = 0
        for top in topics:
            data[tag + "_" + str(ti)] = int(top)
            ti += 1
        outfile = open(out_dir + "/" + docs[dc] + ".topics_" + tag, "w")
        outfile.write(json.dumps(data))
        outfile.close()
        dc += 1
        print dc
    count += 1
