with open("input1.txt") as f:
    lines = f.readlines();
    s = 0
    win = {
        "A": 2,
        "B": 3,
        "C": 1,
    }
    draw = {
        "A": 1,
        "B": 2,
        "C": 3,
    }
    lose = {
        "A": 3,
        "B": 1,
        "C": 2,
    }
    for line in lines:
        line = line.strip()
        arr = line.split(" ")
        if arr[1] == "X":
            s += lose[arr[0]]
        if arr[1] == "Y":
            s += 3 + draw[arr[0]]
        if arr[1] == "Z":
            s += 6 + win[arr[0]]

print(s)
        
