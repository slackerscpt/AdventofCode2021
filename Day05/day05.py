from collections import defaultdict

def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]
        return inputData

def determineXY(data):
    matrix = defaultdict(int)
    matrix2 = defaultdict(int)
    for cords in data:
        x, y = cords.split('->')
        x1, y1 = map(int, x.split(','))
        x2, y2 = map(int, y.split(','))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                matrix[x1, i] += 1
                matrix2[x1, i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                matrix[i, y1] += 1
                matrix2[i, y1] += 1
        else:
            a = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            b = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for x, y in zip(a, b):
                 matrix2[x, y] += 1

    print('Part 1 Solution: %s' %(sum(x > 1 for x in matrix.values())))
    print('Part 2 Solution: %s' %(sum(x > 1 for x in matrix2.values())))

def part1(): 
    data = readFiles()
    determineXY(data)

def part2():
    return


part1()
part2()