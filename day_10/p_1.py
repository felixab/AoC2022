with open("input1.txt") as f:
    lines = f.readlines()
    reg = 1
    arr = []
    for line in lines:
        line = line.strip().split(" ")
        op = line[0]
        print(line)
        if op == "noop":
            arr.append(reg)
            continue
        val = int(line[1])
        for j in range(2):
            if j == 1:
                arr.append(reg)
                reg += val
            else:
                arr.append(reg)


print(arr)
print(arr[19]*20 + arr[59]*60 + arr[99]*100 +
      arr[139]*140 + arr[179] * 180 + arr[219] * 220)
print(arr[19], arr[19]*20)
print(arr[59], arr[59]*60)
print(arr[99], arr[99]*100)
print(arr[139], arr[139]*140)
print(arr[179], arr[179] * 180)
print(arr[219], arr[219] * 220)
