def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]

        return inputData

def createInt(data):
    temp = [int(number) for number in data]
    return temp

def compare(data):
    previous = data[0]
    increased = 0
    decreased = 0
    for numbers in data:
        if numbers > previous:
            increased += 1
            #print ('%s increased' %numbers)
        elif previous > numbers:
            decreased += 1
            #print ('%s decreased' %numbers)
        else: 
            continue

        previous = numbers

    # print ('Increased: %d' %increased)
    # print ('Decreased: %d' %decreased)
    return increased, decreased

def buildPart2(data):
    updatedData = []
    counter = 0
    while (counter < (len(data)-2) ):
        total = data[counter] + data[counter+1] + data[counter+2]
        updatedData.append(total)
        counter = counter + 1
    # print (updatedData)

    return updatedData

def part1():
    data = readFiles()
    data = createInt(data)
    increased, decreased =compare(data)
    print ('Part 1 Solution is: %s' %increased)

def part2():
    data = readFiles()
    data = createInt(data)
    updated = buildPart2(data)
    increased, decreased = compare(updated)
    print ('Part 2 Solution is: %s' %increased)


part1()
part2()