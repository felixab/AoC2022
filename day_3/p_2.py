with open("input1.txt") as f:
    lines = f.readlines();
    matches = []
    index = 0
    temp_count = {}
    for line in lines:
        line = line.strip()
        dups = set()
        if (index) % 3 == 0:
            temp_count = {}
        for char in line:
            if char not in temp_count:
                temp_count[char] = 1
                dups.add(char)
            elif char not in dups:
                temp_count[char] += 1
                dups.add(char)
        
        for key, value in temp_count.items():
            if value == 3:
                matches.append(key)
                break
        index += 1
    
print(sum([ord(c) - 96 if ord(c) - 96 > 0 else ord(c) - 38 for c in matches]))
            