import argparse

def compareLists(firstList, secondList):
    i = 0
    while i < len(firstList) and i < len(secondList):
        if type(firstList[i]) is list and type(secondList[i]) is list:
            returnVal = compareLists(firstList[i], secondList[i])
            if returnVal is not None:
                return returnVal 
            else:
                i += 1
                continue
        elif type(firstList[i]) is list or type(secondList[i]) is list:
            if type(firstList[i]) is int:
                returnVal = compareLists([firstList[i]], secondList[i])
            else:
                returnVal = compareLists(firstList[i], [secondList[i]])
            if returnVal is not None:
                return returnVal 
            else:
                i += 1
                continue
        else:
            if firstList[i] < secondList[i]:
                return True
            elif firstList[i] > secondList[i]:
                return False
            

        i += 1
    if len(firstList) < len(secondList):
        return True
    elif len(firstList) > len(secondList):
        return False
    return None
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()
    lines.append("") 
    i = 0
    j = 1
    total = 0
    while i < len(lines):
        if lines[i] == "":
            firstList = eval(lines[i-2])
            secondList = eval(lines[i-1])
            if compareLists(firstList, secondList):
                total += j
            j += 1
        i += 1
    print(total)
