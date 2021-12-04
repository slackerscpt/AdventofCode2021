def readFiles():
    with open('input.txt', "r") as data:
        inputData = [line.rstrip() for line in data]
        return inputData

def readDirections(data):
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

    # print ('Horizontal: %s' %horizontal)
    # print ('Aim: %s' %aim)
    # print ('Depth: %s' %depth)

    # print ('Total: %d' %(horizontal * depth))

    return horizontal, aim, depth

def part1():
    data = readFiles()
    horizontal, aim, depth = readDirections(data)
    print ('Part 1 Solution is: %s' %(horizontal * aim))

def part2():
    data = readFiles()
    horizontal, aim, depth = readDirections(data)
    print ('Part 2 Solution is: %s' %(horizontal * depth))


part1()
part2()