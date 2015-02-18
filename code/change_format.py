import sys

infile = sys.argv[1]

i = open(infile)
o = open(infile + ".txt", "w")
l = open(infile + ".lbl", "w")

for line in i:
    vals = line.split("\t")
    o.write(vals[0].strip() + "\t" + vals[2].strip() + "\n")
    l.write(vals[0].strip() + "\t" + vals[1].strip() + "\n")

i.close()
o.close()
l.close()
