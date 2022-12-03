with open("input1.txt") as f:
    lines = f.readlines();
    allElvesCalories = []
    currentCalories = 0
    for line in lines:
        line = line.strip()
        if line == "":
            allElvesCalories.append(currentCalories)
            currentCalories = 0
            continue
        currentCalories += int(line)
    allElvesCalories.sort(reverse=True)
    print(allElvesCalories)

print(allElvesCalories[0] + allElvesCalories[1] + allElvesCalories[2])