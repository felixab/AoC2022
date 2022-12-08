class Node:
    def __init__(self, name="/", parent=None, size=0):
        self.children = []
        self.parent = parent
        self.size = size
        self.name = name

    def PrintTree(self):
        print(self.data)


res = 0
arrr = []


def fun_recursion(node):
    global res
    global arrr
    val = 0
    for child in node.children:
        if len(child.children) > 0:
            val += fun_recursion(child)
        else:
            val += child.size
    arrr.append(val)
    return val


with open("input1.txt") as f:
    lines = f.readlines()
    current_node = Node()
    start_pointer = current_node
    for line in lines:
        line = line.strip()
        if line == "$ cd /":
            continue
        commands = line.split(" ")
        if commands[0] == "$":
            if commands[1] == "cd":
                if commands[2] == "..":
                    current_node = current_node.parent
                    continue
                else:
                    print(commands)
                    current_node = [
                        child for child in current_node.children if child.name == commands[2]][0]
        elif commands[0] == "dir":
            current_node.children.append(
                Node(name=commands[1], parent=current_node))
        elif commands[0] != "ls":
            current_node.children.append(
                Node(size=int(commands[0]), name=commands[1], parent=current_node))

    val = fun_recursion(start_pointer)
arrr.sort()
print(val, arrr)
