def isNotVisible(lines, i, j):
    if i == 0 or i == len(lines[0]):
        return False
    if j == 0 or j == len(lines):
        return False
    maximum = int(lines[i][j])
    rowLength = len(lines[0])
    columnLength = len(lines)
    
    found = False
    for k in range(j):
        if int(lines[i][k]) >= maximum:
            found = True
    if not found:
        return False

    found = False
    for k in range(j+1, rowLength):
        if int(lines[i][k]) >= maximum:
            found = True
    if not found:
        return False
    
    found = False
    for k in range(i):
        if int(lines[k][j]) >= maximum:
            found = True
    if not found:
        return False

    found = False
    for k in range(i+1, columnLength):
        if int(lines[k][j]) >= maximum:
            found = True
    if not found:
        return False
    return True
        
with open('day8.txt', 'r') as f:
    lines = f.read().splitlines()

rowLength = len(lines[0])
columnLength = len(lines)
total = 0
for i in range(rowLength):
    for j in range(columnLength):
        if not isNotVisible(lines, i, j):
            print(str(i) + ', ' + str(j))
            total += 1
print(total)
