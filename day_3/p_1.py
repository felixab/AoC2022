with open("input1.txt") as f:
    lines = f.readlines();
    matches = []
    for line in lines:
        line = line.strip()
        index = 0
        mid = len(line) / 2 
        items_dict = {}
        while index < mid:
            items_dict[line[index]] = 1
            index += 1
        while index < len(line):
            if line[index] in items_dict:
                matches.append(line[index])
                break
            index += 1 

print(sum([ord(c) - 96 if ord(c) - 96 > 0 else ord(c) - 38 for c in matches]))
