def isNotVisible(lines, i, j):
    if i == 0 or i == len(lines[0])-1:
        return 0
    if j == 0 or j == len(lines)-1:
        return 0
    print(f'{i}, {j}')
    maximum = int(lines[i][j])
    rowLength = len(lines[0])
    columnLength = len(lines)
    
    left = 0
    for k in range(j-1, -1, -1):
        if int(lines[i][k]) < maximum:
            left += 1
        else:
            left += 1
            break

    right = 0
    for k in range(j+1, rowLength):
        if int(lines[i][k]) < maximum:
            right += 1
        else:
            right += 1
            break

    top = 0
    for k in range(i-1, -1, -1):
        if int(lines[k][j]) < maximum:
            top += 1
        else:
            top += 1
            break

    bottom = 0
    for k in range(i+1, columnLength):
        if int(lines[k][j]) < maximum:
            bottom += 1
        else:
            bottom += 1
            break
    print(f'{left},{top},{right},{bottom}')
    return (left * top * right * bottom)
        
with open('day8.txt', 'r') as f:
    lines = f.read().splitlines()

rowLength = len(lines[0])
columnLength = len(lines)
maximum = 0
for i in range(rowLength):
    for j in range(columnLength):
        result = isNotVisible(lines, i, j)
        if result > maximum:
            maximum = result 
print(maximum)
