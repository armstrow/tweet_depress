import sys
import scipy.io
import scipy
import numpy as np
from numpy import linalg as LA
if len(sys.argv)<4:
	print "we need train_file (corpus.train), count file, gamma file, csv file"
	sys.exit()

train_file = sys.argv[1]
count_file =sys.argv[2]
gamma_file =sys.argv[3]
output_file =sys.argv[4]

count_map =dict()

with open(count_file) as file:
	for line in file:
		values = line.rstrip().split("\t")
		count_map[values[0]] =int(values[1])

user_label=dict()
weekids =list()
with open(train_file) as file:
	for line in file:
		values =line.rstrip().split("\t")
		wid = values[0]
		weekids.append(wid)
		label =values[1]
		if label=="0":
			label="-"
		else:
			label="+"
		id =wid.split("|")[0]
		user_label[id] =label

#read gamma file 
index=0
#gamma =np.loadtxt(gamma_file)
g = open(gamma_file, "r")
gamma = g.read().split("\n")[1:]

num_docs =len(gamma)
print num_docs

user_gamma=dict()
for i in xrange(num_docs):
        if gamma[i] == "":
                continue
        wid = gamma[i].split(',')[0]
	count = count_map[wid]
	v = [float(x) for x in gamma[i].split(",")[1:-1]]
	v = np.multiply(v,count)
	id =wid.split("|")[0]
	#label = user_label[id]

	if id in user_gamma:
		user_gamma[id] = np.add(user_gamma[id],v)
	else:
		user_gamma[id]=v

def convertCsv(vec):
	tmpVec =vec/float(LA.norm(vec,1))
	l =list()
	for i in xrange(len(tmpVec)):
		l.append(str(tmpVec[i]))
	return ','.join(l)

output =open(output_file,'w')
for userid in user_gamma:
	label = user_label[userid]
	csvStr =convertCsv(user_gamma[userid])
	realuser =userid.replace(".tweets","")
	output.write(realuser+","+csvStr+","+label+"\n")

output.close()

