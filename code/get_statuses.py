"""
Extracts text from twitter-scraped files into an easy-to-use csv format.  Does not additional processing of the text, but get_statuses2.py actually tokenizes and does some processing of them.

inputs: 
path - folder containing raw twitter files, 1 file per user, each containing json dictionaries of tweet information (1 tweet per line)
label - label to identify the processed file (+, -) or (0, 1), etc.
set_file (optional) - file listing document ids to be selected for use

outputs:
out_file - name of the output files. 2 will be produced, one with the labels and one with the text

USAGE:
python get_statuses.py path out_file label set_file

example:
python get_statuses.py raw_tweets/ out.csv - dev_set.txt 
"""


from os import listdir
from os.path import isfile, join
import sys
import json
import re
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import csv

sys.path.append('external')
import twokenize

#dev_set = []
#f = open("dev.txt", "r")
#for line in f:
#    dev_set.append(line.strip())
#dev_set = set(dev_set)
#f.close()


mypath = sys.argv[1]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

set_file = None
if len(sys.argv) > 4:
    set_file = sys.argv[4]

dev_set = []
if set_file:
    sfile = open(set_file)
    for line in sfile:
        dev_set.append(line.strip())
dev_set = set(dev_set)

#outfile = open(sys.argv[2], 'ab')
label = sys.argv[3]
#csvwriter = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
csvwriter1 = csv.writer(open(sys.argv[2]+'_label.csv', 'ab'), quoting=csv.QUOTE_MINIMAL, delimiter='\t')
csvwriter2 = csv.writer(open(sys.argv[2]+'_text.csv', 'ab'), quoting=csv.QUOTE_MINIMAL, delimiter='\t')
all_tweets = []
#t = WordPunctTokenizer()
count = 0
r = re.compile("(^|[^A-Za-z0-9_])@[A-Za-z0-9_]{1,16}($|[^A-Za-z0-9_])")
r2 = re.compile("^\w+$")
#csvwriter.writerow(["userid", "avg", "text"])
for fname in onlyfiles:
    if len(dev_set) > 0 and not fname in dev_set:
        continue
    f = open(mypath + "/" + fname, "r")
    tweets = ""
    tweet_count = 0
    for line in f.readlines():
        text = line #json.loads(line)["text"] + " "
        text = text.lower()
        #if "http" in text:
        #    continue
        #text = r.sub(r"\1@\2", text) #remove twitter id's
        #text = r.sub(r"\1@\2", text) #do it twice b/c won't catch consecutive
        tweets += text.strip() + " "
        tweet_count += 1
        #if tweet_count > 25:
        #    break
        
#        pp_tweets = twokenize.tokenizeRawTweetText(text)
#        pp_tweets = filter(lambda w: w not in stopwords.words('english'), pp_tweets)
#        pp_tweets = [w for w in pp_tweets if r2.match(w)]
#        if len(pp_tweets) < 10:
#            continue
#        f_tweets = " ".join(pp_tweets)
#        f_tweets = f_tweets.encode("ascii", "ignore")
#        csvwriter.writerow([fname.split(".")[0] + ":" + str(tweet_count), label,f_tweets])

#    if tweet_count <= 25: #skip users with < 25 tweets
#        continue
    try:
        pp_tweets = twokenize.tokenizeRawTweetText(tweets)
    except:
        continue

    #pp_tweets = filter(lambda w: w not in stopwords.words('english'), pp_tweets)
    pp_tweets = [w for w in pp_tweets if r2.match(w)]
    #f_tweets = tweets
    f_tweets = " ".join(pp_tweets)
#    try:
#        f_tweets = f_tweets.encode("ascii", "ignore")
#    except:
#        continue
    #print fname.split(".")[0] + ",-," + tweets"
    #csvwriter.writerow([fname.split(".")[0] , label,f_tweets])
    tmpFile = open(sys.argv[2] + "/" + fname.split(".")[0], "w")
    tmpFile.write(f_tweets)
    tmpFile.close()
    csvwriter1.writerow([fname.split(".")[0], label])
    csvwriter2.writerow([fname.split(".")[0], f_tweets])
    #all_tweets.append((fname.split(".")[0], f_tweets))
    count += 1
    #if count == 100:
    #    break
    print count

#print count
   
