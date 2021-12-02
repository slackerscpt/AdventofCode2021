from os import read


def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]

        return inputData

def readDirections(data):
    horizontal = 0
    depth = 0
    for directions in data:
        direction, movement = directions.split(" ")
        movement = int(movement)

        if (direction == "forward"):
            horizontal += movement
        if (direction == "down"):
            depth += movement
        if (direction == "up"):
            depth -= movement

    print ('Horizontal: %s' %horizontal)
    print ('Depth: %s' %depth)

    print ('Total: %d' %(horizontal * depth))
    
def readDirectionsp2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for directions in data:
        direction, movement = directions.split(" ")
        movement = int(movement)

        if (direction == "forward"):
            horizontal += movement
            depth += (aim * movement) 
        if (direction == "down"):
            aim += movement
        if (direction == "up"):
            aim -= movement

    print ('Horizontal: %s' %horizontal)
    print ('Aim: %s' %aim)
    print ('Depth: %s' %depth)

    print ('Total: %d' %(horizontal * depth))

def part1():
    data = readFiles()
    readDirections(data)

def part2():
    data = readFiles()
    readDirectionsp2(data)


part1()
part2()