def printboard(xState, zState):
    zero = 'X' if xState[0] else ( 'O' if zState[0] else 0)
    one = 'X' if xState[1] else ( 'O' if zState[1] else 1)
    two = 'X' if xState[2] else ( 'O' if zState[2] else 2)
    three = 'X' if xState[3] else ( 'O' if zState[3] else 3)
    four = 'X' if xState[4] else ( 'O' if zState[4] else 4)
    five = 'X' if xState[5] else ( 'O' if zState[5] else 5)
    six = 'X' if xState[6] else ( 'O' if zState[6] else 6)
    seven = 'X' if xState[7] else ( 'O' if zState[7] else 7)
    eight = 'X' if xState[8] else ( 'O' if zState[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

if __name__ =="__main__":
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("Hey!! welcome to tic tac toe")
    while(True):
        printboard(xState, zState)
        if turn==1:
            print("X's chance ")
            value= int (input("please enter the value: "))
            xState[value]=1
        else:
            print("O's chance ")
            value= int (input("please enter the value: "))
            zState[value]=1
        turn=1-turn
        ######## X's case##################
        if xState[0]+xState[1]+xState[2]==3:
            printboard(xState, zState)
            print("X wins!!!")
            break
        elif xState[3]+xState[4]+xState[5]==3:
            printboard(xState, zState)
            print("X wins!!!")
            break
        elif xState[6]+xState[7]+xState[8]==3:
            printboard(xState, zState)
            print("X wins!!!")
            break
        elif xState[0]+xState[4]+xState[8]==3:
            printboard(xState, zState)
            print("X wins!!!")
            break
        elif xState[2]+xState[4]+xState[6]==3:
            printboard(xState, zState)
            print("X wins!!!")
            break
        ################## Z's case##############
        if zState[0]+zState[1]+zState[2]==3:
            printboard(xState, zState)
            print("O wins!!!")
            break
        elif zState[3]+zState[4]+zState[5]==3:
            printboard(xState, zState)
            print("O wins!!!")
            break
        elif zState[6]+zState[7]+zState[8]==3:
            printboard(xState, zState)
            print("O wins!!!")
            break
        elif zState[0]+zState[4]+zState[8]==3:
            printboard(xState, zState)
            print("O wins!!!")
            break
        elif zState[2]+zState[4]+zState[6]==3:
            printboard(xState, zState)
            print("O wins!!!")
            break
        

