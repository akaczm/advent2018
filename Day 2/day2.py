import string

# Part 1
done_dubs = []
done_tris = []
c = [0,0]

with open('input.txt') as f:
    
    for index, line in enumerate(f.readlines()):
        for char in string.ascii_lowercase:
            if line.count(char) == 2 and index not in done_dubs:
                done_dubs.append(index)
            
            if line.count(char) == 3 and index not in done_tris:
                done_tris.append(index)

    print(len(done_dubs) * len(done_tris))

# Part 2

import itertools

with open('input.txt') as f:
    lines = f.readlines()
    for a, b in itertools.combinations(lines, 2):
        diffs = 0
        diffindex = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diffs += 1
                diffindex = i
        if diffs == 1:
            print(a)
            print(b)
            newstr = a[:diffindex] + a[diffindex+1:]
            print(newstr)