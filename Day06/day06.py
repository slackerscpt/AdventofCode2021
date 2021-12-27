def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]
        return inputData


def createInt(data):
    temp = []
    for numbers in data:
        for numb in numbers.split(','):
            temp.append(int(numb))

    return temp

def runLife(data):
    rounds = 0
    while (rounds < 256):
        temp = []
        counter = 0
        addCount = 0
        for numbers in data:
            if numbers == 0:
                addCount += 1
                data[counter] = 6
            else:
                data[counter] = (numbers -1)
            counter += 1

        while (addCount > 0):
            data.append(8)
            addCount -= 1
        rounds +=1
        print ('Round: %s' %rounds)
    print (len(data))


def part1(): 
    data = readFiles()
    data = createInt(data)
    runLife(data)
def part2():
    return


part1()
part2()