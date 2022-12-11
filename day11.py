import argparse

class Monkey:
    def __init__(self, integer, starting_items, operation, test, ifTrueMonkey, ifFalseMonkey):
        self.integer = integer
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.frequency = 0
        self.ifTrueMonkey = ifTrueMonkey
        self.ifFalseMonkey = ifFalseMonkey
    def __str__(self):
        return f"{self.integer}: {str(self.items)}, {self.operation}, {self.test}, {self.ifTrueMonkey}, {self.ifFalseMonkey}"
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    lines.append("") 
    monkeyList = []
    i = 0
    while i < len(lines):
        if not lines[i]:
            # Monkey 0
            monkeyNum = int(lines[i-6][7])
            # Starting items
            monkeyItems = list(map(lambda x: int(x), lines[i-5].split(': ', 1)[1].split(', ')))
            operation = lines[i-4].split(' = ', 1)[1]
            test = int(lines[i-3].split(' by ')[1])
            ifTrueMonkey = int(lines[i-2].split('monkey ', 1)[1])
            ifFalseMonkey = int(lines[i-1].split('monkey ', 1)[1])
            monkey = Monkey(monkeyNum, monkeyItems, operation, test, ifTrueMonkey, ifFalseMonkey)

            monkeyList.append(monkey)
        i += 1
    

    # Run through rounds
    i = 0
    while i < 10000:
        print(i)
        for monkey in monkeyList:
            while monkey.items:
                handleItem = monkey.items.pop(0)
                monkey.frequency += 1
                old = handleItem
                handleItem = eval(monkey.operation)
                # divide by 3 and round down to nearest integer
                #handleItem = int(handleItem / 3)
                resultOfTest = handleItem % monkey.test == 0
                if resultOfTest: # if true
                    monkeyList[monkey.ifTrueMonkey].items.append(handleItem)
                else:
                    monkeyList[monkey.ifFalseMonkey].items.append(handleItem)
                #print(handleItem, resultOfTest)

                print(monkey.items)
        i += 1

    copyMonkeyList = monkeyList.copy()
    copyMonkeyList.sort(key=lambda x: x.frequency)
    print(copyMonkeyList[len(copyMonkeyList) - 1].frequency)
    print(copyMonkeyList[len(copyMonkeyList) - 2].frequency)
