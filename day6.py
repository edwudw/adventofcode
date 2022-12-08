
if __name__ == '__main__':
    with open('day6.txt', 'r') as f:
        lines = f.read().splitlines()
    line = lines[0]
    i = 0
    while i < len(line) - 14:
        latest = line[i:i+14]
        print(latest)
        i += 1
        if len(set(latest)) == len(latest):
            print(str(i+13))
            break

