"""
Makes predictions using an SVM based on the training and test sets given as input parameters, both in the format "<id>,<f1>,<f2>,...,<label>" where the first row is a header row, and subsequent rows are the id, a comma separated list of feature values and a binary label (0, 1).  The label in the test file will be ignored.  The output is a list of rows, 1 per id in the test set in the format "<id>,<confidence>" where confidence is a continuous value representing the SVM's decision value for classifying each row.

USAGE: svm.py train_set.csv test_set.csv out_file.csv
"""

from sklearn import svm
import sys

infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])


train = []
train_labels = []
test = []
test_ids = []
test_labels = []

for line in infile1:
    if line.startswith("id,"):
        continue
    vals = line.strip().split(",")
    train.append(vals[1:-1])
    train_labels.append(vals[-1])
infile1.close()

for line in infile2:
    if line.startswith("id,"):
        continue
    vals = line.strip().split(",")
    test.append(vals[1:-1])
    test_labels.append(vals[-1])
    test_ids.append(vals[0])
infile2.close()

clf = svm.SVC(probability=True, kernel='linear')
clf.fit(train, train_labels)
clf.predict(test)
predictions = clf.decision_function(test)
outfile = open(sys.argv[3], "w")
for i in range(0, len(test)):
    outfile.write(test_ids[i] + "," + str(predictions[i][0]) + "\n")
outfile.close()
