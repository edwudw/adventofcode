import argparse
from functools import cmp_to_key

def compareLists(firstList, secondList):
    i = 0
    while i < len(firstList) and i < len(secondList):
        if type(firstList[i]) is list and type(secondList[i]) is list:
            returnVal = compareLists(firstList[i], secondList[i])
            if returnVal != 0:
                return returnVal 
            else:
                i += 1
                continue
        elif type(firstList[i]) is list or type(secondList[i]) is list:
            if type(firstList[i]) is int:
                returnVal = compareLists([firstList[i]], secondList[i])
            else:
                returnVal = compareLists(firstList[i], [secondList[i]])
            if returnVal != 0:
                return returnVal 
            else:
                i += 1
                continue
        else:
            if firstList[i] < secondList[i]:
                return -1
            elif firstList[i] > secondList[i]:
                return 1
            

        i += 1
    if len(firstList) < len(secondList):
        return -1
    elif len(firstList) > len(secondList):
        return 1
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    result = []
    i = 0
    while i < len(lines):
        if lines[i] != "":
            result.append(eval(lines[i]))
        i += 1
    result.append([[2]])
    result.append([[6]])
    result.sort(key=cmp_to_key(compareLists))
    i = 0
    for res in result:
        if res == [[2]]:
            print(i+1)
        elif res == [[6]]:
            print(i+1)
        i += 1
