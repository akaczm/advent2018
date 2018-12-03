import string


done_dubs = []
done_tris = []
c = [0,0]

with open('input.txt') as f:
    for index, line in enumerate(f.readlines()):
        for char in string.ascii_lowercase:
            if line.count(char) == 2 and index not in done_dubs:
                done_dubs.append(index)
        for char in string.ascii_lowercase:
            if line.count(char) == 3 and index not in done_tris:
                done_tris.append(index)
                break
            
    print(len(done_dubs) * len(done_tris))