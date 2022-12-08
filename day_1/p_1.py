with open("input1.txt") as f:
    lines = f.readlines()
    maxCalories = 0
    currentCalories = 0
    for line in lines:
        line = line.strip()
        if line == "":
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
            continue
        currentCalories += int(line)
        
print(maxCalories)
        
        