import math

with open("input2.txt") as f:
    lines = f.readlines()
    visited = set()
    visited.add((0, 0))
    # H, 1, 2, ... , 8, 9
    # x, y
    knots_curr = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                  [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    knots_last = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
                  [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for line in lines:
        line = line.strip().split(" ")
        direction = line[0]
        steps = int(line[1])
        for step in range(steps):
            for idx, knot in enumerate(knots_curr):
                print("LAST_CURR", knots_last, knots_curr, idx)
                if idx == 0:
                    if direction == "L":
                        knots_curr[idx][0] -= 1
                    if direction == "R":
                        knots_curr[idx][0] += 1
                    if direction == "D":
                        knots_curr[idx][1] -= 1
                    if direction == "U":
                        knots_curr[idx][1] += 1
                else:
                    print("math", math.sqrt((knots_curr[idx][0] - knots_curr[idx-1][0]) ** 2 + (
                        knots_curr[idx][1] - knots_curr[idx-1][1]) ** 2))
                    if (math.sqrt((knots_curr[idx][0] - knots_curr[idx-1][0]) ** 2 + (knots_curr[idx][1] - knots_curr[idx-1][1]) ** 2) >= 2):
                        knots_curr[idx] = knots_last[idx-1]
                    knots_last[idx] = knots_curr[idx]
                    if idx == 9:
                        visited.add(
                            (knots_last[idx-1][0], knots_last[idx-1][1]))

print(visited)
