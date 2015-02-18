import sys

andy = open("andy_tops.txt")
mine = open(sys.argv[1])

andy_tops = {}
for line in andy:
    words = line.split()
    andy_tops[words[0]] = words[1:]

my_tops = []
for line in mine:
    if line[0] != "[":
        continue
    words = line.split()
    my_tops.append(words[3:])

def correlate(top1, top2):
    count = 0
    for word in top1:
        if word in top2:
            count += 1
    return count

out_file = open(sys.argv[1] + ".labeled", "w")
for top in my_tops:
    scores = {}
    for label, top2 in andy_tops.items():
        scores[label] = correlate(top, top2)
    out_file.write(str(max(scores.values())) + " " +max(scores, key=scores.get) + " " + " ".join(top) + "\n")
out_file.close()

