
if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        lines = f.read().splitlines()
    horizontal = 0
    aim = 0
    depth = 0
    for line in lines:
        total = line.split(' ')
        direction = total[0]
        magnitude = int(total[1])
        if direction == 'forward':
            horizontal += magnitude
            depth += (aim * magnitude)
        elif direction == 'backward':
            horizontal -= magnitude
        elif direction == 'up':
            aim -= magnitude
        else:
            aim += magnitude
    print(horizontal)
    print(depth)
    print(horizontal * depth)
