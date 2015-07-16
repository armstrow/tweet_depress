'''
Converts a csv of predictions to a roc curve.  The "truth" file is hard coded below, and the input parameter is the csv file to use with 1 row per id in the format "<id>,<confidence>" where confidence is a continuous value representing the decision value for classifying each row.

depends on pyroc.py available from github:
https://gitbhub.com/marcelcaraciolo/PyROC
'''

import sys
sys.path.append("/home/will/tweet_depress/code")

import pyroc


truth = open("Paper/pred_results/truth.csv")

true_vals = {}
for line in truth:
    if line.strip() == '':
        continue
    vals = line.strip().split("\t")
    true_vals[vals[1]] = int(vals[0])

roclist = []
labels = []
for fname in sys.argv[1:]:
    infile = open(fname)
    data = []
    for line in infile:
        if line.strip() == '':
            continue
        vals = line.strip().split(",")
        if not vals[0] in true_vals:
            continue
        data.append((true_vals[vals[0]], float(vals[1])))

    roc = pyroc.ROCData(data)
    print fname + ": " + str(roc.auc())
    roclist.append(roc)
    labels.append(";".join([x for x in fname.split("/")[-1].split("_")[0:-1] if x != ""]))

pyroc.plot_multiple_roc(roclist, labels=labels)
