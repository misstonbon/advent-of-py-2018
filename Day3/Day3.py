import numpy as np

file_input = list(map(str.strip, open("./daythree.txt").readlines()))


def get_claim(line):
    _, _, border, dimensions = line.split()
    left, top = [int(d) for  d in border[:-1].split(",")]
    width, height = [int(x) for x in dimensions.split("x")]
    return (top, top + height, left, left + width)

fabric = np.zeros((1000, 1000))

def get_overlap(file):
    for line in file_input:
        x_min, x_max, y_min, y_max = get_claim(line)
        fabric[x_min:x_max, y_min:y_max] += 1
    return np.count_nonzero(fabric > 1)

print(get_overlap(file_input))
# 101469

def all_claims(file):
    claims = []
    for line in file_input:
        id, _, border, dimensions = line.split()
        id = id[1:]
        left, top = [int(d) for d in border[:-1].split(",")]
        width, height = [int(x) for x in dimensions.split("x")]
        claims.append((id, (top,top + height, left, left + width)))
    return claims

claims = all_claims(file_input)
for _, (x_min, x_max, y_min, y_max) in claims:
    fabric[x_min:x_max, y_min:y_max] += 1
    for id,(x_min, x_max, y_min, y_max) in claims:
        if np.count_nonzero(fabric[x_min:x_max, y_min:y_max] != 1) == 0:
            print(id)
            exit()
#1067