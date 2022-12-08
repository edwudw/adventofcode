def getSumSliding(lines, i):
    slice = lines[i-2:i+1]
    slice = list(map(lambda x: int(x), slice))
    total = sum(slice)
    with open('test.txt', 'a') as f:
        f.write(str(slice) + '\n')
        f.write(str(total) + '\n')

    return sum(slice)

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        lines = f.read().splitlines()
    total = 0
    i = 3
    while i < len(lines):
        sliceSum = getSumSliding(lines, i-1)
        previousSliceSum = getSumSliding(lines, i)
        if sliceSum < previousSliceSum:
            total += 1
        i += 1
    print(total)
