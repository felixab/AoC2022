with open("input1.txt") as f:
    lines = f.readlines();
    count = 0
    for line in lines:
        line = line.strip()
        pairs = line.split(",")
        one = pairs[0].split("-")
        two = pairs[1].split("-")
        if int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1]):
            count += 1
        elif int(two[0]) <= int(one[0]) and int(two[1]) >= int(one[1]):
            count += 1

print(count)