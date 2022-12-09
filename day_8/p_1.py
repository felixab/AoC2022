with open("input1.txt") as f:
    lines = f.readlines()
    trees = []
    tree_set = set()
    for line in lines:
        tree_row = []
        line = list(line.strip())
        for tree in line:
            tree_row.append(int(tree))
        trees.append(tree_row)

    for j, tree_rows in enumerate(trees):
        max = -1
        for i, tree in enumerate(tree_rows):
            if tree > max:
                tree_set.add((i, j))
                max = tree
    print(len(tree_set))
    for j, tree_rows in enumerate(trees):
        max = -1
        for i, tree in enumerate(reversed(tree_rows)):
            if tree > max:
                tree_set.add((i, j))
                max = tree
    print(len(tree_set))
    i = 0
    while i < len(trees[0]):
        max = -1
        j = 0
        while j < len(trees):
            tree = trees[j][i]
            if tree > max:
                tree_set.add((i, j))
                max = tree
            j += 1
        i += 1
    print(len(tree_set))
    i = 0
    while i < len(trees[0]):
        max = -1
        j = len(trees) - 1
        while j >= 0:
            tree = trees[j][i]
            if tree > max:
                tree_set.add((i, j))
                max = tree
            j -= 1
        i += 1

    print(len(tree_set) - 1)
