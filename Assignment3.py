# candy crush Game

elements = ['🔥','🚀','❤','😍']
boardlist = []

# randomly populate 25 items in the board list

import random

random.choice(elements)

def generateNewBoard():
    boardlist = []
    for items in range(25):
        boardlist.append(random.choice(elements))
    return boardlist
boardlist = generateNewBoard()

def printBoard(list):
    print("our Emoji crush board")
    pos = 0
    for i in range(5):
        for j in range(5):
            print(list[pos],end = " ")
            pos = pos+1
        print("")
boardlist = generateNewBoard()
printBoard(boardlist)

def takeInput():
    currentpos = input("Enetr the position of items you want to move: ")
    futurepos = input("Enetr the new position: ")
    return [currentpos,futurepos]

def boardRef():
    print( "Our Emoji crush board reference")
    pos = 0
    for i in range(5):
        for j in range(5):
            print(pos,end = " ")
            pos = pos+1
        print("")
boardRef()

# make a function to get all possible combinations to check for matching
# Check for valid combinations for Emoji crush and then only send it else dnt send it

def getCombinations(num):

    #horizontal combination
    c1 = [num - 2, num - 1, num]
    c2 = [num, num + 1, num + 2]
    c3 = [num - 1, num, num + 1]

    # check for horizontal valid combinations

    horizontal_row = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
    horizontal_comb = [c1,c2,c3]

    valid_horizontal_comb = []

    for hc in horizontal_comb:
        for hr in horizontal_row:
            if(all(items in hr for items in hc)):
                valid_horizontal_comb.append(hc)

    #print(valid_horizontal_comb)

    # vertical combinations

    c4 = [num - 10,num -5,num]
    c5 = [num,num + 5,num + 10]
    c6 = [num - 5,num,num + 5]

    vertical_comb = [c4,c5,c6]
    valid_vc = []
    for vc in vertical_comb:
        flag = 0
        for position in vc:
            if position<0 or position>24:
                flag = 1
        if flag == 0:
            valid_vc.append(vc)

    #print(valid_vc)

    list = valid_horizontal_comb
    list.extend(valid_vc)
    return list
getCombinations(0)

# make a function to check if there is a match

printBoard(boardlist)

def checkmatch(currentpos, futurepos, boardlist):

    ele = boardlist[currentpos]
    combos = getCombinations(futurepos)

    flag = 0

    for combo in combos:
        if(boardlist[combo[0]] == ele and boardlist[combo[1]] == ele) or (boardlist[combo[1]]
        == ele and boardlist[combo[2]] == ele ) or (boardlist[combo[0]] == ele and boardlist[combo[2]] == ele):
            flag = 1
    if flag == 1:
        print("Wow its match 😍 ")
    else:
        print("its not match try again 😔")

#checkmatch(18,23,boardlist)
#checkmatch(0,1,boardlist)
checkmatch(0,2,boardlist)







