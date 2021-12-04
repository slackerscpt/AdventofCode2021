def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]

        return inputData

def compare(data):
    previous = 0
    increased = 0
    decreased = 0
    for numbers in data:
        print ('Number: %s' %numbers)
        print ('Previous: %s' %previous)
        if (previous == 0):
            print('Starting')
        else:
            if int(numbers) > previous:
                increased += 1
                print ('%s increased' %numbers)
            elif previous > int(numbers):
                decreased += 1
                print ('%s decreased' %numbers)
            else: 
                print ('%s no change' %numbers)

        previous = int(numbers)

    print ('Increased: %d' %increased)
    print ('Decreased: %d' %decreased)


def compare2(data):
    previous = 0
    increased = 0
    decreased = 0
    for numbers in data:
        print ('Number: %s' %numbers)
        print ('Previous: %s' %previous)
        if (previous == 0):
            print('Starting')
        else:
            if numbers > previous:
                increased += 1
                print ('%s increased' %numbers)
            elif previous > numbers:
                decreased += 1
                print ('%s decreased' %numbers)
            else: 
                print ('%s no change' %numbers)

        previous = numbers

    print ('Increased: %d' %increased)
    print ('Decreased: %d' %decreased)

def buildPart2(data):
    updatedData = []
    counter = 0
    while (counter < (len(data)-2) ):
        print ('Counter: %d' %counter)
        print (len(data)-2)
        temp = data[counter]
        temp1 = data[counter+1]
        temp2 = data[counter+2]
        total = int(temp) + int(temp1) + int(temp2)
        print (total)
        updatedData.append(total)
        print (total)
        print (data[counter +2])
        counter = counter + 1
    print (updatedData)

    return updatedData



def part1():
    data = readFiles()
    compare(data)

def part2():
    data = readFiles()
    updated = buildPart2(data)
    compare2(updated)


part1()
#part2()