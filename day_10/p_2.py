with open("input1.txt") as f:
    lines = f.readlines()
    reg = 1
    arr = []
    res = []
    res.append([])
    index = 0
    level = 0
    x = 0
    for line in lines:
        x = index % 40
        line = line.strip().split(" ")
        op = line[0]
        if op == "noop":
            if x >= reg - 1 and x <= reg + 1:
                res[level].append("#")
            else:
                res[level].append(".")
            index += 1
            if index % 40 == 0 and index != 0:
                res.append([])
                level += 1
            continue
        val = int(line[1])
        for j in range(2):
            x = index % 40
            if x >= reg - 1 and x <= reg + 1:
                res[level].append("#")
            else:
                res[level].append(".")
            if j == 1:
                reg += val
            index += 1
            if index % 40 == 0 and index != 0:
                res.append([])
                level += 1


for r in res:
    print("".join(r))
