import re
if __name__ == '__main__':
    stacks = [
        ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
        ['J', 'V', 'B', 'C', 'Z', 'F'],
        ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
        ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
        ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
        ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
        ['L', 'G', 'C', 'Z', 'V'],
        ['N', 'L', 'G'],
        ['J', 'F', 'H', 'C']
    ]
    with open('day5.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        numbers = re.findall(r'\d+', line)
        numbers = list(map(lambda x: int(x), numbers))
        column1 = numbers[1] - 1
        column2 = numbers[2] - 1
        n = numbers[0]
        temp = stacks[column1][-n:]
        del stacks[column1][-n:]
        stacks[column2] += temp
    print(stacks)
    total = ""
    for i in stacks:
        if len(i) > 0:
            total += (i[len(i)-1])
    print(total)
