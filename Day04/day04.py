from collections import Counter
from os import read


def readFiles():
    with open('input.txt', "r") as data:
    #with open ('test.txt', "r")  as data:
        inputData = [line.rstrip() for line in data]

        return inputData

def getBingoNumbers(data):
    numbers = data.pop(0)
    #Remove white space
    data.pop(0)
    return numbers, data
    

def getBoards(data):
    index = 0
    board = []
    allBoards = []
    for lines in data:
        if lines == '':
            allBoards.append(board)
            board= []
        else:
            line = []
            for numbers in lines.split():
                line.append(numbers)
            board.append(line)


    return allBoards



def playBingoToLose(calledNumbers, boards):
    finalNumber = -1
    winningBoard = ''
    for called in calledNumbers.split(','):
        boards = markedCalled(called, boards)
        boards = checkBoardp2(boards)
        if (len(boards) == 1):
            #have to capture last board
            winningBoard = boards[0]
        if (len(boards) == 0):
            #when we have 0 remaining, we need to know number that solved it. 
            finalNumber = called
            break


    finalPart2(finalNumber, winningBoard)

def playBingo(calledNumbers, boards):
    finalNumber = -1
    winningBoard = ''
    for called in calledNumbers.split(','):
        boards = markedCalled(called, boards)
        solved, winningBoard = checkBoard(boards)
        if (solved):
            finalNumber = called
            winningBoard = winningBoard
            break

    finalPart1(finalNumber, winningBoard)


def finalPart1(number, board):
    # print ('Winner')
    # print (number)
    # print (board)
    sum = 0
    for lines in board:
        for numbers in lines:
            if numbers != 'X':
                sum += int(numbers)

    # print (sum)
    # print (sum * int(number))
    print ('Part 1 Solution: %s' %(sum * int(number)))
    
def finalPart2(number, board):
    # print ('Winner')
    # print (number)
    # print (board)
    sum = 0
    for lines in board:
        for numbers in lines:
            if numbers != 'X':
                sum += int(numbers)

    # print (sum)
    # print (sum * int(number))
    print ('Part 2 Solution: %s' %(sum * int(number)))

def markedCalled(number, boards):
    for board in boards:
        for boardNumbers in board:
            for numbers in range(len(boardNumbers)):
                if boardNumbers[numbers] == number:

                    boardNumbers[numbers] = 'X'

    return boards

def checkBoardp2(boards):
    #We need to think how can we win
    # Straight across
    # Straight down
    # diagnial
    #each board is a matrix
    # x,0 x,1 x,2 x,3 x,4 across
    # 0,0 1,1 2,2 3,3 4,4 dig 1
    # 0,4 1,3 2,2 3,1 4,1 dig 2
    for board in boards:
        digCheck = checkDig(board)
        horizCheck = checkHoriz(board)
        # print (digCheck)
        # print (horizCheck)
        if (digCheck or horizCheck):
            boards.remove(board)
    return (boards)

def checkBoard(boards):
    #We need to think how can we win
    # Straight across
    # Straight down
    # diagnial
    #each board is a matrix
    # x,0 x,1 x,2 x,3 x,4 across
    # 0,0 1,1 2,2 3,3 4,4 dig 1
    # 0,4 1,3 2,2 3,1 4,1 dig 2
    for board in boards:
        digCheck = checkDig(board)
        horizCheck = checkHoriz(board)
        # print (digCheck)
        # print (horizCheck)
        if (digCheck or horizCheck):
            return (True, board)
    return (False, False)

def checkHoriz(board):
    solved = False
    for row in range(0,5):
        if (board[row][0] == 'X'):
            if (board[row][1] == 'X'):
                if (board[row][2] == 'X'):
                    if (board[row][3] == 'X'):
                        if (board[row][4] == 'X'):
                            solved = True

    for row in range(0,5):
        if (board[0][row] == 'X'):
            if (board[1][row] == 'X'):
                if (board[2][row] == 'X'):
                    if (board[3][row] == 'X'):
                        if (board[4][row] == 'X'):
                            solved = True
    return solved

def checkDig(board):
    solved = False
    if (board[0][0] == 'X'):
        if (board[1][1] == 'X'):
            if (board[2][2] == 'X'):
                if (board[3][3] == 'X'):
                    if (board[4][4] == 'X'):
                        solved = True
    if (board[0][4] == 'X'):
        if (board[1][3] == 'X'):
            if (board[2][2] == 'X'):
                if (board[3][1] == 'X'):
                    if (board[4][0] == 'X'):
                        solved = True
                        
    return solved

    


def part1():
    data = readFiles()
    calledNumbers, data = getBingoNumbers(data)
    boards = getBoards(data)
    playBingo(calledNumbers, boards)


def part2():
    data = readFiles()
    calledNumbers, data = getBingoNumbers(data)
    boards = getBoards(data) 
    playBingoToLose(calledNumbers, boards)


part1()
part2()