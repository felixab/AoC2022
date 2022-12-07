with open("input1.txt") as f:
    lines = f.readlines();
    lo = 1
    hi = 4
    chars = lines[0]
    d = {chars[0]: 1, chars[1]: 2,chars[2]: 1}
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
        if len(d.keys()) == 4:
            break
        lo += 1
        hi += 1

    print(hi + 1)