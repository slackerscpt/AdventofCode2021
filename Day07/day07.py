from collections import Counter

def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]
        return inputData


def parse_input(data):
    temp = []
    for numbers in data:
        return sorted(list(map(int, numbers.split(','))))

def determineFuel(data):
    median = data[len(data) // 2]

    fuel_used = list(map(lambda x: abs(x - median), data))

    print (sum(fuel_used))

def newFuel(data):
    mean = sum(data) //len(data)
    distance_moved = list(map(lambda x: abs(x - mean), data))
    fuel_used = list(map( lambda x: x * (x + 1)/2, distance_moved))

    print (sum(fuel_used))
def part1(): 
    data = readFiles()
    data = parse_input(data)
    determineFuel(data)

def part2():
    data = readFiles()
    data = parse_input(data)
    newFuel(data)


part1()
part2()