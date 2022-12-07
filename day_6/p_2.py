with open("input1.txt") as f:
    lines = f.readlines();
    lo = 1
    hi = 14
    chars = lines[0]
    d = {
        "q": 1, 
        "z": 2,
        "b": 1,
        "w": 4,
        "g": 1,
        "h": 3,
        "d": 2,
    }
    while hi < len(chars):
        if chars[hi] in d:
            d[chars[hi]] += 1
        else:
            d[chars[hi]] = 1
        if chars[lo - 1] in d:
            d[chars[lo - 1]] -= 1
            if d[chars[lo - 1]] == 0:
                del d[chars[lo - 1]]
        else:
            print("what")
        if len(d.keys()) == 14:
            break
        lo += 1
        hi += 1

    print(hi + 1)