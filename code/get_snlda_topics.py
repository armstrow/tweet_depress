import sys

infile = open(sys.argv[1])
idfile = open(sys.argv[2])

labels = []
for line in idfile:
    vals = line.strip().split("\t")
    labels.append(vals)

idfile.close()

count = 0
outfile = open(sys.argv[3], "w")
for line in infile:
    vals = line.strip().split("\t")
    if count == 0:
        header = "id,"
        for i in range(0, len(vals[1:])):
            header += str(i) + ","
        header += "label"
        outfile.write(header + "\n")
    new_row = [labels[count][0]] + vals[1:] + [labels[count][1]]
    count += 1
    outfile.write(",".join(new_row) + "\n")
outfile.close()
infile.close()
