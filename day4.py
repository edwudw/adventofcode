import re
def overlapping(x1, x2, y1, y2):
    if x1 <= y2 and x2 >= y1:
        return True
    return False
    #if x1 <= y1 and x2 >= y2:
    #    return True
    #if y1 <= x1 and y2 >= x2:
    #    return True
    #return False
if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        lines = f.read().splitlines()
    total = 0
    for line in lines:
        numbers = re.findall(r'\d+', line)
        numbers = list(map(lambda x: int(x), numbers))
        if overlapping(numbers[0], numbers[1], numbers[2], numbers[3]):
            total += 1
    print(total)
 
