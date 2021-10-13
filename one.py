txt_file = open("input.txt", "r")
lines = txt_file.readlines()

map = {}

for line in lines:
    line = line.strip('\n')
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in map.keys():
            map[word] += 1
        else:
            map[word] = 1

print(map)