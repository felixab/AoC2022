with open("input1.txt") as f:
    lines = f.readlines()
    trees = []
    tree_set = set()
    res = 0
    for line in lines:
        tree_row = []
        line = list(line.strip())
        for tree in line:
            tree_row.append(int(tree))
        trees.append(tree_row)

    for j in range(len(trees)):
        for i in range(len(trees[0])):
            current = trees[j][i]
            # l, r, t ,b
            scenics = [0, 0, 0, 0]
            k = i - 1
            while k >= 0:
                if trees[j][k] < current:
                    scenics[0] += 1
                else:
                    scenics[0] += 1
                    break
                k -= 1
            k = i + 1
            while k < len(trees[0]):
                if trees[j][k] < current:
                    scenics[1] += 1
                else:
                    scenics[1] += 1
                    break
                k += 1
            l = j - 1
            while l >= 0:
                if trees[l][i] < current:
                    scenics[2] += 1
                else:
                    scenics[2] += 1
                    break
                l -= 1
            l = j + 1
            while l < len(trees):
                if trees[l][i] < current:
                    scenics[3] += 1
                else:
                    scenics[3] += 1
                    break
                l += 1
            score = 0
            for scenic in scenics:
                if score == 0:
                    score += scenic
                else:
                    score *= scenic
            if score > res:
                res = score

print(res)
