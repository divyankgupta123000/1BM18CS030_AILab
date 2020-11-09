#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_board(a):
    print("", a[1], " │", a[2], " │ ", a[3], " ")
    print("────┼────┼────")
    print("", a[4], " │", a[5], " │ ", a[6], " ")
    print("────┼────┼────")
    print("", a[7], " │", a[8], " │ ", a[9], " ")


# for display the instruction of game
def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()

    players[0] = input("Player 1 : ")
    players[1] = "AI"

    if players[1] == "C" or players[1] == "c":
        players[1] = "Computer"
        print("\n-------- Instructions ---------")
        print("->", players[0], "you will be using X")
        print("->", players[1], "will be using 0")
        print("-> Turn starts from", players[0])
        print("-> Potisions are like :-")
        print("  1 │  2 │ 3  ")
        print("────┼────┼────")
        print("  4 │ 5  │ 6  ")
        print("────┼────┼────")
        print("  7 │ 8  │ 9  ")
        print("-> press S to start the game")
        flag = input()
        return flag
    else:
        print("\n-------- Instructions ---------")
        print("->", players[0], "you will be using X")
        print("->", players[1], "will be using 0")
        print("-> Turn starts from", players[0])
        print("-> Potisions are like :-")
        print("  1 │  2 │ 3  ")
        print("────┼────┼────")
        print("  4 │ 5  │ 6  ")
        print("────┼────┼────")
        print("  7 │ 8  │ 9  ")
        print("-> press S to start the game")
        flag = input()
        return flag


# for start the game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nThis is your turn", players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\n\nHurray !!,", players[0], "you win !!!")
                break
        else:
            print("\nThis is your turn", players[1])
            p = int(input("Please Enter postion : "))
            v = '0'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\nHurray !!,", players[1], "you win !!!")
                break
    else:
        print("\n\nGame is Tied")


def playcomp():
    f = print_instructions()
    if f == "S" or f == "s":
        startcomp()
    else:
        print("Invalid Input")


def startcomp():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nThis is your turn", players[0])
            p = int(input("Please Enter postion : "))
            v = 'x'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\n\nHurray !!,", players[0], "you win !!!")
                break
        else:
            v = "0"
            j = logic(v)
            print("" * 20, "Computer's Turn", "" * 20)
            pos[j] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\nHurray !!,", players[1], "you win !!!")
                break

    else:
        print("\n\nGame is Tied")


def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner


def logic(v):
    if "0" not in pos:
        if pos[5] == " ":
            return 5
        else:
            return 1
    else:
        c = 0
        m = 0
        an = tuple()
        awin = 0
        maxa = 0
        tupa = tuple()
        for t in winning_conditions:
            c, awin = 0, 0
            if (pos[t[0]] == "0" and pos[t[1]] == "0" and pos[t[2]] == " ") or (
                    pos[t[0]] == " " and pos[t[1]] == "0" and pos[t[2]] == "0") or (
                    pos[t[0]] == "0" and pos[t[1]] == " " and pos[t[2]] == "0"):
                c = 2
                if pos[t[0]] == " ":
                    return t[0]
                elif pos[t[1]] == " ":
                    return t[1]
                else:
                    return t[2]


            if (pos[t[0]] == "x" and pos[t[1]] == "x" and pos[t[2]] == " ") or (
                    pos[t[0]] == " " and pos[t[1]] == "x" and pos[t[2]] == "x") or (
                    pos[t[0]] == "x" and pos[t[1]] == " " and pos[t[2]] == "x"):
                if pos[t[0]] == " ":
                    return t[0]
                elif pos[t[1]] == " ":
                    return t[1]
                else:
                    return t[2]

        if pos[3]==" ":
            return 3
        elif pos[6]==" ":
            return 6
        elif pos[9]==" ":
            return 9
        return pos.index(" ")


# main code
pos = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = ['', '']
winning_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
playcomp()


# In[ ]:




