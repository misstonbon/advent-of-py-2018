import collections

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
print( checksum) #7470

print(len(twice))
print(len(three_times))