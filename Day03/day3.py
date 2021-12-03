from typing import get_args


def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]

        return inputData


def countOccurances(numbers, position):
    zero = 0
    one = 0
    for values in numbers:
        if (values[position] == "0"):
            zero += 1
        else:
            one += 1

    return (zero, one)

def setCO2Scrubber(data):
    #for each position, we will keep the most common, or if equal 1
    updatedData = data
    position = 0
    while (position < 12):
        startingData = determineNumbers(updatedData)
        mostCommon = findLeastCommon(position, startingData)
        #print ('Least Common: %s' %mostCommon)
        #print ('Position: %s' %position)
        updatedData = keepCommon(mostCommon, position, updatedData)
        #print (updatedData)
        #print (len(updatedData))
        if (len(updatedData) == 1):
            position = 12
        position += 1

    #print (updatedData[0])
    return updatedData[0]
    


def setOxyNumber(data):
    #for each position, we will keep the most common, or if equal 1
    updatedData = data
    position = 0
    while (position < 12):
        startingData = determineNumbers(updatedData)
        mostCommon = findMostCommon(position, startingData)
        #print ('Most Common: %s' %mostCommon)
        #print ('Position: %s' %position)
        updatedData = keepCommon(mostCommon, position, updatedData)
        if (len(updatedData) == 1):
            position = 12
        position += 1
        #print (updatedData)

    #print (updatedData[0])
    return str(updatedData[0])

def keepCommon(mostCommon, position, data):
    updatedData = []
    for numbers in data:
        if numbers[position] == str(mostCommon):
            updatedData.append(numbers)

    return updatedData  

def findLeastCommon(position, collectionData):
    zero, one = collectionData[position]
    if (zero > one ):
        return 1
    else:
        return 0

def findMostCommon(position, collectionData):
    zero, one = collectionData[position]
    if (zero > one ):
        return 0
    else:
        return 1

def setEpNumber(collectionData):
    gamma = {}
    epsilon  = {}
    for positions in collectionData:
        zero, one = collectionData[positions]
        if (zero > one):
            gamma[positions]= 0
            epsilon[positions] = 1
        else:
            gamma[positions]= 1
            epsilon[positions] = 0   

    gammaStr = ''
    for number in gamma:
        gammaStr += str(gamma[number])
    epsilonStr = ''
    for number in epsilon:
        epsilonStr += str(epsilon[number])

    a = int(gammaStr, 2)
    b = int(epsilonStr, 2)

    print ('Part 1 Answer: %s' %(a * b))

def determineNumbers(data):
    numberList = []
    for numbers in data:
        numberList.append(list(numbers))

    position = 0
    collectionData = {}
    while (position < len(data[0])):
        (zero, one ) = countOccurances(data, position)
        collectionData[position] = (zero, one)
        position += 1

    return collectionData




def part1():
    data = readFiles()
    collectionData = determineNumbers(data)
    setEpNumber(collectionData)


def part2():
    data = readFiles()
    OxyNumber = setOxyNumber(data)
    data = readFiles()
    Co2Number = setCO2Scrubber(data)
    a= (int(OxyNumber, 2))
    b =(int(Co2Number, 2))
    print ('Part 2 Answer: %s' %(a*b))



part1()
part2()