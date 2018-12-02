import collections
from itertools import combinations

with open('daytwo.txt', 'r') as file:
    content = file.readlines()
    lines = []
    for line in content:
        lines.append(line[:-1])

counts = {}
for line in lines:
    counts[line] = collections.Counter(line)

twice = set()
three_times = set()

for key in counts:
    for letter, count in counts[key].items():
        if count == 2 and key not in twice:
            twice.add(key)
        if count == 3  and key not in three_times:
            three_times.add(key)

checksum = len(twice) * len(three_times)
print(checksum) #7470

sameSame = []

words = list(counts.keys())

def oneAway(str1, str2):
    difference = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            difference += 1
    return difference

for i in range(len(words)):
    for j in range(i+1, len(words) - 1 ):
        if oneAway(words[i], words[j]) == 1 and len(words[i]) == len(words[j]):
            sameSame.append(words[i])
            sameSame.append(words[j])
     
print(sameSame)
# kqzxdenujwcstybmgvyiofrrd