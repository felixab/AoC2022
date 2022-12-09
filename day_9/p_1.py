import math

with open("input1.txt") as f:
    lines = f.readlines()
    visited = set()
    visited.add((0, 0))
    t_x = 0
    t_y = 0
    h_x = 0
    h_y = 0
    l_h_x = 0
    l_h_y = 0
    lastDir = None
    for line in lines:
        line = line.strip().split(" ")
        direction = line[0]
        steps = int(line[1])
        for step in range(steps):
            if direction == "L":
                h_x -= 1
                # distance bigger than 2
                if (math.sqrt((t_x - h_x) ** 2 + (t_y - h_y) ** 2) >= 2):
                    visited.add((l_h_x, l_h_y))
                    t_x = l_h_x
                    t_y = l_h_y
                l_h_x = h_x

            if direction == "R":
                h_x += 1
                # distance bigger than 2
                if (math.sqrt((t_x - h_x) ** 2 + (t_y - h_y) ** 2) >= 2):
                    visited.add((l_h_x, l_h_y))
                    t_x = l_h_x
                    t_y = l_h_y
                l_h_x = h_x
            if direction == "U":
                h_y += 1
                # distance bigger than 2
                if (math.sqrt((t_x - h_x) ** 2 + (t_y - h_y) ** 2) >= 2):
                    visited.add((l_h_x, l_h_y))
                    t_x = l_h_x
                    t_y = l_h_y
                l_h_y = h_y
            if direction == "D":
                h_y -= 1
                # distance bigger than 2
                if (math.sqrt((t_x - h_x) ** 2 + (t_y - h_y) ** 2) >= 2):
                    visited.add((l_h_x, l_h_y))
                    t_x = l_h_x
                    t_y = l_h_y
                l_h_y = h_y
print(len(visited))
