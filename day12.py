import argparse
import sys

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.x},{self.y}'


class QueueObj:
    def __init__(self, coords, steps=0, stepList=[]):
        self.coords = coords
        self.steps = steps
        self.stepList = stepList
    def __str__(self):
        return f'{self.coords.x},{self.coords.y}'
    def __repr__(self):
        return self.__str__()

def bfs(currX, currY):
    queue = [QueueObj(Coords(currX, currY))]
    visited = set()
    while len(queue) > 0:
        queueObj = queue.pop(0)
        curr = queueObj.coords
        visited.add(f'{curr.x},{curr.y}')
        if lines[curr.x][curr.y] == 'E':
            return queueObj.steps

        potentialCoords = [Coords(curr.x - 1, curr.y), Coords(curr.x + 1, curr.y), Coords(curr.x, curr.y - 1), Coords(curr.x, curr.y + 1)]
        for coord in potentialCoords:
            if coord.x < 0 or coord.x >= columnLength:
                continue
            if coord.y < 0 or coord.y >= rowLength:
                continue
            value = ord(lines[coord.x][coord.y])
            currValue = ord(lines[curr.x][curr.y])
            if lines[curr.x][curr.y] == 'S':
                currValue = 96
            elif lines[coord.x][coord.y] == 'E':
                return queueObj.steps+1
                
            if currValue >= value or currValue+1 == value:
                if f'{coord.x},{coord.y}' not in visited:
                    queue.append(QueueObj(coord, queueObj.steps+1, queueObj.stepList + [coord]))
                    visited.add(f'{coord.x},{coord.y}')
    return 999999999999999999999999999



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    rowLength = len(lines[0])
    columnLength = len(lines)
    a_letters = []
    for x in range(columnLength):
        for y in range(rowLength):
            if lines[x][y] == "a":
                a_letters.append((x,y))
    smallest = 9999999999999999 
    for a in a_letters:
        result = bfs(a[0], a[1])
        if result < smallest:
            smallest = result
    print(smallest)
