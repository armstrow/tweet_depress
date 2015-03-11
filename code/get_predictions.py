import sys
import sys
import scipy.io
import scipy
import numpy as np
from numpy import linalg as LA

gamma_file = open(sys.argv[1], "r")
count_file = sys.argv[2]
out_file = open(sys.argv[3], "w")


count_map =dict()

with open(count_file) as file:
	for line in file:
		values = line.rstrip().split("\t")
		count_map[values[0]] =int(values[1])


#read gamma file 
index=0
#gamma =np.loadtxt(gamma_file)
gamma = gamma_file.read().split("\n")[1:]

num_docs =len(gamma)
print num_docs

user_gamma=dict()
user_count_total = dict()
for i in xrange(num_docs):
        if gamma[i] == "":
                continue
        wid = gamma[i].split('\t')[0]
	count = count_map[wid]
	v = float(gamma[i].split("\t")[-1])
	v = v * count
	id =wid.split("|")[0]
	#label = user_label[id]

	if id in user_gamma:
		user_gamma[id] += v
                user_count_total[id] += count
	else:
		user_gamma[id]=v
                user_count_total[id] = count


allVals = user_gamma.items()
users = [x[0] for x in allVals]
vals = [x[1] for x in allVals]

norm_vals = []

for count in range(0, len(users)):
    new_val = vals[count] / float(user_count_total[users[count]])
    norm_vals.append((users[count], new_val))


for item in sorted(norm_vals, key=lambda x: x[1])[::-1]:
    out_file.write(str(item[0]) + "," + str(item[1]) + "\n")

out_file.close()

