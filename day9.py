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

    if abs(tailX - x) >= 2:
        if direction == 'R':
            tailX += 1
        else:
            tailX -= 1
        if tailY != y:
            tailY = y
    elif abs(tailY - y) >= 2:
        if direction == 'U':
            tailY += 1
        else:
            tailY -= 1
        if tailX != x:
            tailX = x
    return (tailX, tailY)    

if __name__ == '__main__':

    with open('day9.txt', 'r') as f:
        lines = f.read().splitlines()
    head = (0,0)
    tail = (0,0)
    visitedSet = set()
    for line in lines:
        lineSplit = line.split(' ', 1)
        direction = lineSplit[0]
        magnitude = int(lineSplit[1])
        for i in range(magnitude):
            head = applyDirection(direction, head)
            tail = getTail(direction, head, tail)
            tailCoords = f"{str(tail[0])},{str(tail[1])}"
            if tailCoords not in visitedSet:
                visitedSet.add(tailCoords)
    print(len(visitedSet))
