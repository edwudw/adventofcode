def getCommonLetter(line1, line2, line3):
    firstSet = set(line1)
    secondSet = set(line2)
    thirdSet = set(line3)
    common = firstSet.intersection(secondSet)
    common = common.intersection(thirdSet)
    return common.pop()

def getPriority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1

if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        lines = f.read().splitlines()
    total = 0
    i = 0
    lineBuffer = []
    for line in lines:
        lineBuffer.append(line)
        i += 1
        if i >= 3:
            common = getCommonLetter(lineBuffer[0], lineBuffer[1], lineBuffer[2])
            priority = getPriority(common)
            total += priority
            lineBuffer = []
            i = 0
    print(total)
