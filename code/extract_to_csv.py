import sys
import os
import json

mydir = sys.argv[1]
outfile = open(sys.argv[2], "w")
#control = "input/raw/control"
#dep = "input/raw/depressed"
#control = "anonymized_control_tweets"
#dep = "anonymized_depression_tweets"
label_file = open("input/raw/control_depression/controldepression.users.train")
labels = {}
for line in label_file:
    vals = line.split("\t")
    labels[vals[0].strip().split(".")[0]] = vals[1].strip()

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
    if labels[uid] == "0":
        s += "-"
        #elif uid in dep_ids:
    elif labels[uid] == "1":
        s += "+"
    else:
        print "user not found"
        continue
    outfile.write(s + "\n")
outfile.close()
