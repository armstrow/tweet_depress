'''
Converts a prediction file output by SLDA/SNLDA for aggregated tweets into a csv with a single continuous prediction per author.  

Usage:
python get_predictions.py <prediction_file> <count_of_tweets_per_aggregation_unit> <output_file>

example:
python get_predictions.py output/SNLDA_30_4/twitter/train/models/RANDOM_SNLDA_Ks-30-4_B-250_M-1000_L-25_a-1-1_b-0.25-0.1-0.05_p-0.2-0.2_g-100-10_r-0.1_m-0_s-0.01-0.5-2.5_opt-false_bin-false_path-NONE_root-false/te_result/predictions input/DC/DC.clean.main.fold0.dev.count results/snlda.csv

note the aggregation count file has the format "<id>|<tag>\t<count>" where each line is the count of tweets in that aggregation unit, which will serve to weight the prediction for that unit in the overall prediction.
'''

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

