with open("input1.txt") as f:
    lines = f.readlines();
    line_index = 0
    stacks = {}
    for line in lines:
        if line_index == 8:
            break
        line_index += 1
        stack_index = 1
        space_index = 0
        for val in line.strip().split(" "):
            if val != "" :
                if stack_index not in stacks:
                    stacks[stack_index] = [val]
                else:
                    stacks[stack_index].insert(0, val)
                stack_index += 1
                space_index = 4
            else:
                space_index -= 1
            if space_index == 0:
                stack_index += 1
                space_index = 4
    
    line_index = 0
    for line in lines:
        if line_index > 9:
            line = line.strip().split(" ")
            qty = int(line[1])
            first = int(line[3])
            second = int(line[5])
            count = 0
            while count < qty:
                val = stacks[first].pop()
                stacks[second].append(val)
                count += 1
        line_index += 1
    
    lst = [None] * 9
    for key, value in stacks.items():
        lst[key - 1] = value[len(value) - 1][1]

    print(lst)