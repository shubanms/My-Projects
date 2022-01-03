import random
import numpy as np

Board=[]
Board_q=[]
list1=[]
for i in range(1,10):
    list1.append(i)


for i in range(len(list1)):
    j = random.randint(0, (len(list1))-1)
    element=list1.pop(j)
    list1.append(element)
Board.append(list1)

def rotate(l, n):
    return l[n:] + l[:n]

list2=(rotate(list1,3))
Board.append(list2)

list3=(rotate(list2,3))
Board.append(list3)

list4=(rotate(list3,1))
Board.append(list4)

list5=(rotate(list4,3))
Board.append(list5)

list6=(rotate(list5,3))
Board.append(list6)

list7=(rotate(list6,1))
Board.append(list7)

list8=(rotate(list7,3))
Board.append(list8)

list9=(rotate(list8,3))
Board.append(list9)

print("1 - Very easy")
print("2 - Easy")
print("3 - Moderate")
print("4 - Tough")
print("")
n=int(input("Enter the puzzle difficulty: "))

for j in range(n):
    for i in range(9):
        Board[i][random.randint(0, 8)]=0


count=0
for i in range(9):
    for j in range(9):
        if Board[i][j]==0:
            count=count+1
        else:
            pass

print("")

print("Sudoku Puzzle")
print("Number of empty boxes: ",count)
print("Number of filled number's: ",(81-int(count)))
print("")
print(np.matrix(Board))


def possible(x,y,n):
        global Board
        for i in range(0,9):
                if Board[y][i] == n:
                        return False
        for i in range(0,9):
                if Board[i][x] == n:
                        return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range (0,3):
                for j in range (0,3):
                        if Board[y0+i][x0+j] == n:
                                return False
        return True

def solve():
        global Board
        for y in range(9):
                for x in range(9):
                        if Board[y][x] == 0:
                                for n in range(1,10):
                                        if possible(x,y,n):
                                                Board[y][x] = n
                                                solve()
                                                Board[y][x] = 0
                                return
        print("")
        print("Solution Board")
        print("")
        print(np.matrix(Board))

print("")
print("1 - Show solution")
print("2 - Exit")
print("")

n1=int(input("Enter your choice: "))
if n1 == 1:
    solve()
if n1 == 2:
    print("")
    print("Thank you")

