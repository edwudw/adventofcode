class Tree:
    def __init__(self, name, type, size, children):
        self.name = name
        self.type = type
        self.size = size
        self.children = children

lines = []
lineNum = 1
def generateTree(name, level):
    global lines
    global lineNum
    curr = lines[0]
    lines = lines[1:]
    lineNum += 1
    children = {}
    total_size = 0
    print((" " * (level - 1)) + name)
    while curr != "$ cd .." and lines:
        curr_split = curr.split(' ', 1)
        print('currName: ' + name + ': ' + str(curr_split))
        if curr[:len("$ cd")] == "$ cd":
            # is a directory
            dir_name = curr[len("$ cd "):]

            children[dir_name] = generateTree(dir_name, level+1)
            total_size += children[dir_name].size
            #print('total so far: ' + str(children[dir_name].size))
            #print('TOTAL SIZE: ' + str(total_size))
        elif curr_split[0] != '$' and curr_split[0] != 'dir':
            # is a file
            file_name = curr_split[1]
            file_size = int(curr_split[0])
            children[file_name] = Tree(file_name, "file", file_size, {})
            #print(file_size)
            total_size += file_size
            #print('total so far: ' + str(total_size))
        if not lines:
            break
        curr = lines[0]
        lines = lines[1:]
        lineNum += 1
    
    if len(lines) == 0:
        curr_split = curr.split(' ', 1)
        print('currName: ' + name + ': ' + str(curr_split))
        if curr_split[0] != '$' and curr_split[0] != 'dir':
            # is a file
            file_name = curr_split[1]
            file_size = int(curr_split[0])
            children[file_name] = Tree(file_name, "file", file_size, {})
            #print(file_size)
            total_size += file_size
    ## print(level)
    print((" " * (level - 1)) + "ending: " + name + ', ' + str(total_size))
    
    ## print('line: ' + str(lineNum))
    return Tree(name, "dir", total_size, children)

def fixSize(tree):
    total = 0
    for child in tree.children:
        if tree.children[child].type == 'dir':
            fixSize(tree.children[child])
        total += tree.children[child].size
    tree.size = total      
        

total = 0
def readTree(tree):
    global total
    if tree.type == 'dir' and tree.size <= 100000:
        #print(tree.name + ', ' + str(tree.size))
        total += tree.size
    for child in tree.children:
        readTree(tree.children[child])

if __name__ == "__main__":
    total = 0
    with open('day7.txt') as f:
        lines = f.read().splitlines()
    lines = lines[1:]
    main = generateTree("/", 1)
    # # fixSize(main)
    readTree(main)
    print(total)
