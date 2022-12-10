def applyDirection(direction, coords):
    x = coords[0]
    y = coords[1]
    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    elif direction == "U":
        y += 1
    else:
        y -= 1
    return (x, y)


def getTail(direction, head, tail):
    x = head[0]
    y = head[1]
    tailX = tail[0]
    tailY = tail[1]

    if abs(tailY - y) >= 2:
        if y - tailY > 0:
            tailY += 1
        else:
            tailY -= 1
        if tailX != x:
            tailX = x
    elif abs(tailX - x) >= 2:
        if x - tailX > 0:
            tailX += 1
        else:
            tailX -= 1
        if tailY != y:
            tailY = y
    return (tailX, tailY)    

def generateHeads():
    total = []
    for i in range(10):
        total.append((0, 0))
    return total

if __name__ == '__main__':

    with open('day9.txt', 'r') as f:
        lines = f.read().splitlines()
    head = (0,0)
    tail = (0,0)
    heads = generateHeads()
    visitedSet = set()
    for line in lines:
        lineSplit = line.split(' ', 1)
        direction = lineSplit[0]
        magnitude = int(lineSplit[1])
        for i in range(magnitude):
            heads[0] = applyDirection(direction, heads[0])
            for j in range(len(heads) - 1):
                heads[j+1] = getTail(direction, heads[j], heads[j+1])
            print(heads)
            tail = heads[len(heads) - 1]
            # tailCoords = f"{tail[0]},{tail[1]}"
            if tail not in visitedSet:
                visitedSet.add(tail)
    print(len(visitedSet))
