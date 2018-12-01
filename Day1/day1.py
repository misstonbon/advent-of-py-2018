with open('dayone.txt', 'r') as file:
    content = file.readlines()
    lines = []
    for line in content:
        lines.append(int(line))


#516
startingFreq = 0
frequencies = set()
frequencies.add(startingFreq)

while True:
    for line in lines: 
        startingFreq += line
        if startingFreq in frequencies:
            print("Found %d " % startingFreq )
            exit()
        else:
            frequencies.add(startingFreq)
