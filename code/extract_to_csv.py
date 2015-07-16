"""
Used as an intermediary step in run.py for converting topic assignments to a more usabel csv file.  Takes as input a directory containing 1 json file per document consisting of an object a label for each topic mapped to the count of occurances of that topic in the document and a label file with one row per document in the format "<id>\t<label>".  Output is a file with one row per document in the format "<id>,<c1>,<c2>,...,<label>", where c1 through cn are the counts of topic occurances from the input directory.

Usage:
python extract_to_csv.py input_dir outfile label_file
"""

import sys
import os
import json

mydir = sys.argv[1]
outfile = open(sys.argv[2], "w")
#control = "input/raw/control"
#dep = "input/raw/depressed"
#control = "anonymized_control_tweets"
#dep = "anonymized_depression_tweets"
label_file = open(sys.argv[3])
labels = {}
for line in label_file:
    vals = line.split("\t")
    labels[vals[0].strip().split(".")[0]] = vals[1].strip()
label_file.close()
'''label_file = open(sys.argv[3] + "dev.lbl")
for line in label_file:
    vals = line.split("\t")
    labels[vals[0].strip().split(".")[0]] = vals[1].strip()
label_file.close()
label_file = open(sys.argv[3] + "test.lbl")
for line in label_file:
    vals = line.split("\t")
    labels[vals[0].strip().split(".")[0]] = vals[1].strip()
'''

#control_ids = set([x.split(".")[0] for x in os.listdir(control)])
#print control_ids
#dep_ids = set([x.split(".")[0] for x in os.listdir(dep)])
outfile.write("id," + ",".join([str(i) for i in range(0,50)]) + ",label\n")
for fname in os.listdir(mydir):
    f = open(mydir + "/" + fname)
    tail = fname[fname.find("SLDA"):]
    d = json.loads(f.read().strip())
    num_tops = len(d.keys())
    uid = fname.split(".")[0]
    s = uid + ","
    for i in range(0, num_tops):
        s += str(d[tail+"_"+str(i)]) + ","
    #if uid in control_ids:
    if labels[uid] == "0" or labels[uid] == "0.0":
        s += "0"
        #elif uid in dep_ids:
    elif labels[uid] == "1" or labels[uid] == "1.0":
        s += "1"
    else:
        print "user not found"
        continue
    outfile.write(s + "\n")
outfile.close()
