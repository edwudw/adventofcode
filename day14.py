import argparse
import sys

def drawLine(start, end, lines, lowestX):
    startSplit = start.split(',')
    startX = int(startSplit[0]) - lowestX
    startY = int(startSplit[1])
    endSplit = end.split(',')
    endX = int(endSplit[0]) - lowestX
    endY = int(endSplit[1])
    
    if startX == endX:
        start = min(startY, endY)
        end = max(startY, endY)
        for i in range(start, end+1):
            lines[i][startX] = '#'
    else:
        start = min(startX, endX)
        end = max(startX, endX)
        for i in range(start, end+1):
            try:
                lines[startY][i] = '#'
                print(startY, i)
            except:
                print(startY, i)
                sys.exit(1)

def printWorld(world):
    for line in world:
        print(''.join(line))

def sandCanGoHere(world, coords):
    if world[coords[1]][coords[0]] == ".":
        return True
    return False

def applySand(world, lowestX, highestX, highestY):
    curr = (500 - lowestX, 0)
    count = 0
    while True:
        
        if curr[1] + 1 > highestY:
            break
        if sandCanGoHere(world, (curr[0], curr[1]+1)):
            curr = (curr[0], curr[1]+1)
        elif curr[0] - 1 < 0:
            print('break1')
            break
        elif curr[0] - 1 >= 0 and sandCanGoHere(world, (curr[0]-1, curr[1]+1)):
            curr = (curr[0] - 1, curr[1]+1)
        elif curr[0] + 1 > (highestX - lowestX):
            print(curr[0])
            print(highestX - lowestX)
            print('break2')
            break
        elif curr[0] + 1 <= (highestX - lowestX) and sandCanGoHere(world, (curr[0] + 1, curr[1]+1)):
            curr = (curr[0] + 1, curr[1]+1)
        elif world[curr[1]][curr[0]] == '.':
            world[curr[1]][curr[0]] = 'S'
            count += 1
            curr = (500 - lowestX, 0)
        else:
            break
    return count

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    world = []
    lowestX = 1000
    highestX = 0
    highestY = 0
    for line in lines:
        lineSplit = line.split(" -> ")
        for coord in lineSplit:
            coords = coord.split(',')
            coordX = int(coords[0])
            coordY = int(coords[1])
            if coordX < lowestX:
                lowestX = coordX
            if coordX > highestX:
                highestX = coordX
            if coordY > highestY:
                highestY = coordY
    print(lowestX, highestX, highestY)
    lowestX = 0
    highestX = 1000
    world = []
    # world[y][x] because its backwards for some reason
    for i in range(highestY + 3):
        row = []
        for j in range(highestX - lowestX + 1):
            if i == highestY + 2:
                row.append("#")
            else:
                row.append(".")
        world.append(row)
    
    printWorld(world)
    #Finished building environment

    for line in lines:
        lineSplit = line.split(" -> ")
        for i in range(len(lineSplit) - 1):
            drawLine(lineSplit[i], lineSplit[i+1], world, lowestX)
    world[0][500 - lowestX] = '+'
    highestY += 2
    print(applySand(world, lowestX, highestX, highestY))
    #printWorld(world)
