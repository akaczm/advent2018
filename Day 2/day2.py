import string


done_dubs = []
done_tris = []

with open('testinput.txt') as f:
    for index, line in enumerate(f.readlines()):
        for char in string.ascii_lowercase:
            if line.count(char) == 2 and index not in done_dubs:
                done_dubs.append(index)
                print(f"Found dubs in index {index}")
            if line.count(char) == 3 and index not in done_tris:
                done_tris.append(index)
                print(f"Found tris in index {index}")
                break
            
    print(len(done_dubs) * len(done_tris))