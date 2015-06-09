import sys

#andy = open("andy_tops.txt")
andy = open(sys.argv[2])
mine = open(sys.argv[1])

andy_tops = {}
count = 0
for line in andy:
    if line[0] != "[":
        continue
    words = line.split()
    andy_tops[str(count)] = words[3:]
    count += 1
#    words = line.split()
#    andy_tops[words[0]] = words[1:]

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
score = 0
for top in my_tops:
    scores = {}
    for label, top2 in andy_tops.items():
        scores[label] = correlate(top, top2)
    score += max(scores.values())
    out_file.write(str(max(scores.values())) + " " +max(scores, key=scores.get) + " " + " ".join(top) + "\n")
out_file.close()
print score

