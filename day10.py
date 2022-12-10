import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    cycle = 0
    x = 1
    total = 0
    signalStrengthTest = {20, 60, 100, 140, 180, 220}
    while len(lines) > 0:
        line = lines.pop(0)
        lineSplit = line.split(' ', 1)
        if (cycle + 1) in signalStrengthTest:
            # during cycle, calculate signal strength
            total += (x * (cycle+1))
            print(x * (cycle+1))
        if len(lineSplit) == 1:
            # noop
            # update cycle after it has completed
            cycle += 1
        else:
            # addx number
            magnitude = int(lineSplit[1])
            cycle += 1
            if (cycle + 1) in signalStrengthTest:
                # during cycle, calculate signal strength
                total += (x * (cycle+1))
                print(x * (cycle+1))
            x += magnitude
            cycle += 1
    if (cycle+1) in signalStrengthTest:
        # during cycle, calculate signal strength
        total += (x * (cycle+1))
        print(x * (cycle+1))
    print('x: ' + str(x))
    print('cycle: ' + str(cycle))
    print(total) 
