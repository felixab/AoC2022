with open("input1.txt") as f:
    lines = f.readlines();
    s = 0
    vals = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }
    for line in lines:
        line = line.strip()
        arr = line.split(" ")
        if arr[1] == "X":
            s += 1
        if arr[1] == "Y":
            s += 2
        if arr[1] == "Z":
            s += 3
        s += vals[line]

print(s)
        
