
from site import execsitecustomize
import random
import time 
import os
from tracemalloc import start

start = time.time()

def menu():
    print("1:one player  2:two player")
    c=int(input("Enter your choice:"))
    return c

def show_game_board() :
    for i in range(3):
        for j in range(3):
            if game[i][j] =='X':    
                print(CRED + game[i][j]+ CEND,end=' ')
            elif game[i][j]=='O':
                print(CGRN+ game[i][j] + CEND, end=' ')
            elif game[i][j]=='_':
                print(game[i][j], end=' ')        
        print() 

def checking_error(c):
    while True:

        print("player 1")
        while True :
            row = int(input('satr ra vared kon: '))
            col = int(input('sotoun ra vared kon: '))
            if 0<=row<=2 and 0<=col<=2 :
                if game[row][col]== '_' :
                    game[row][col]= 'X'
                    break
                else:
                    print("cell is not empty!")
            else:
                print("index out of range, try again") 
        show_game_board()
        check()               

        print("player 2")
        while True :
            if c==2 : 
            
                row = int(input("shomare satr: "))
                col = int(input("shomare sotoun: "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game[row][col]== '_' :
                        game[row][col] = 'O'
                        break
                    else:
                        print("cell is not empty!")
                else:
                    print("index out of range, try again")        
       
        #show_game_board()
        #check()
            if c==1 :

                row = random.randint(0,2)
                col = random.randint(0,2)
                if game[row][col]== '_' :
                    game[row][col] = 'O'
                    break
                else:
                    print("cell is not empty!")
            
        show_game_board()
        check()
                

def check():
    #sharte tasavi
    b=0
    for i in range(3):
        for j in range(3): 
            if game[i][j]== '_' :
                b+=1
    if b==0 :
        print("**player 1 = player 2**")
        print("Time: " , int( time.time() - start) )
        exit()               
    #check kardane satri
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X' :
            print("player 1 Wins")
            print("Time: ", int( time.time() - start) )
            exit()
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O' :  
            print("player 2 Wins")
            print("Time: ", int( time.time() - start) )
            exit()
    #check kardane sotuni
    for j in range(3): 
        if game[0][j]=='X' and game[1][j]=='X' and game[2][j]=='X' :
            print("player 1 Wins")
            print("Time: " , int( time.time() - start) )
            exit()
        if game[0][j]=='O' and game[1][j]=='O' and game[2][j]=='O' :
            print("player 2 Wins")
            print("Time: " , int( time.time() - start) )
            exit() 
    #check kardan zarbdari        
    if game[0][0]=='X' and game[1][1]=='X' and game[2][2]=='X' :
        print("player 1 Wins")
        print("Time: " , int( time.time() - start) )
        exit()
    if game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O' :
        print("player 2 Wins")
        print("Time: " , int( time.time() - start) )
        exit()
    if game[0][2]=='X' and game[1][1]=='X' and game[2][0]=='X' :
        print("player 1 Wins")
        print("Time: " , int( time.time() - start) )
        exit()
    if game[0][2]=='O' and game[1][1]=='O' and game[2][0]=='O' :
        print("player 2 Wins")
        print("Time: " , int( time.time() - start) )
        exit()                                  

game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

print("Time: " + str( time.time() - start) )
CEND='\033[0m'
CRED='\033[91m'
CGRN='\033[92m'
show_game_board()
c=menu()
checking_error(c)


    