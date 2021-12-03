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


def setCo2Number(collectionData, data):
    mostCommon = findMostCommon(0, collectionData)
    data = keepCommon(mostCommon, 0, data)


def keepCommon(mostCommon, position, data):
    updatedData = []
    for numbers in data:
        print (type(numbers[position]))
        if numbers[0] == str(mostCommon):
            updatedData.append(numbers)

    return updatedData  

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
    #setEpNumber(collectionData)




def part1():
    data = readFiles()
    collectionData = determineNumbers(data)
    setEpNumber(collectionData)


def part2():
    data = readFiles()
    collectionData = determineNumbers(data)
    setCo2Number(collectionData, data)



part1()
part2()