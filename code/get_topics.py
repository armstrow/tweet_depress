'''
Used as an intermediary step in collecting results in run.py.  Turns an assignment file extracted from a "report" zip output by the code in segan into a directory of json dictionaries containing topic counts (used as input to extract_to_csv.py). 

Usage:
python get_topics.py assignment_file docinfo_file out_dir tag

where docinfo_file is the *.docinfo file from the format folder produced in the preprocessing scripts of segan (contains "<id>\t<label>"), and tag is an identifying tag for the set that will be appended to each dictionary entry.
'''


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
