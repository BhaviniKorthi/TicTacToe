#importing random
import random

#Intiallizing the values of the dictionary with empty spaces
game_board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}


#Defining a function to print the tic-tac-toe board
def print_board(game_board):
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", game_board[1], "|", game_board[2], "|", game_board[3], "|")
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", game_board[4], "|", game_board[5], "|", game_board[6], "|")
    print("+", "-", "+", "-", "+", "-", "+")
    print("|", game_board[7], "|", game_board[8], "|", game_board[9], "|")
    print("+", "-", "+", "-", "+", "-", "+")

#Taking input in a two player game
def enter_input1(count):
    if count % 2 == 0:
        index_number = int(input("select a grid from 1 to 9: "))
        if index_number in Range:
            game_board[index_number] = "X"
            Range.remove(index_number)
        else:
            print("TRY AGAIN!!")
            print("WRONG INPUT")
            exit()
    else:
        index_number = int(input("Select a grid from 1 to 9: "))
        if index_number in Range:
            game_board[index_number] = "O"
            Range.remove(index_number)
        else:
            print("TRY AGAIN!!")
            print("WRONG INPUT")
            exit()



#Taking input in the player vs computer game
def enter_input2(count):
    if count % 2 == 0:
        index_number = int(input("Select a grid from 1 to 9: "))
        if index_number in Range:
            index.remove(index_number)
            game_board[index_number] = "X"
            Range.remove(index_number)
        else:
            print("TRY AGAIN!!")
            print("WRONG INPUT")
            exit()
    else:
        index_number = random.choice(index)
        if index_number in Range:
            index.remove(index_number)
            game_board[index_number] = "O"
            Range.remove(index_number)
        else:
            print("TRY AGAIN!!")
            print("WRONG INPUT")
            exit()



#Defining a function to check all the rows
def check_rows(game_board):
    for i in range(1,8,3):
        if game_board[i] == game_board[i + 1] and game_board[i]!=" ":
            if game_board[i] == game_board[i + 2]:
                return True
    return False


#Defining a functions to check all the columns
def check_columns(game_board):
    for i in range(1, 4):
        if game_board[i] == game_board[i + 3] and game_board[i]!=" ":
            if game_board[i] == game_board[i + 6]:
                return True
    return False



#Defining a function to check all the diagonals
def check_diagonals(game_board):
    if game_board[5] != " ":
        if (game_board[5] == game_board[1]) and (game_board[5] == game_board[9]):
            return True
        elif (game_board[5] == game_board[3]) and (game_board[5] == game_board[7]):
            return True
    return False




#Checking whether the game is end or not
def win_or_not():
    if check_rows(game_board):
        return True
    elif check_columns(game_board):
        return True
    elif check_diagonals(game_board):
        return True
    else:
        return False


#Asking the user to select the type of game they want to play
print("Select one option: ")
print("1. Play with friend")
print("2. Play with computer")
option = int(input())
Range=[1,2,3,4,5,6,7,8,9]

#If the user chooses to play with his friend
if option == 1:
    #Taking the name of first player as input
    player_1 = input("Enter the name of first player: ")
    #Taking the name of second player as input
    player_2 = input("Enter the name of second player: ")
    #calling print_board() function to print the tic-tac-toe board
    print_board(game_board)
    #loop to repeat the iterations and continue the game
    for count in range(9):
        #calling the enter_input1() function to take the input
        enter_input1(count)
        #calling the print_board() function to print the tic-tac-toe board after every input
        print_board(game_board)
        if count >= 2:
            #checking whether the game has completed or not
            if win_or_not():
                #Displaying the winner
                if count % 2 == 0:
                    print(player_1, "won the game")
                    print("CONGRATULATIONS!!")
                    #ending the game
                    exit()
                else:
                    print(player_2, "won the game")
                    print("CONGRATULATIONS!!")
                    #ending the game
                    exit()

#If the user chooses to play with the computer
elif option == 2:
    #list to store all the indices to be picked by the computer
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #calling print_board() function to print the tic tac toe board
    print_board(game_board)
    #loop to repeat the iterations and continue the game
    for count in range(9):
        #calling enter_input2() function to take the input from the player
        enter_input2(count)
        print("__________________")
        print()
        #calling print_board function print the tic-tac-toe board after each input
        print_board(game_board)
        #checking whether the game has completed or not to print the result
        if win_or_not():
            #Displaying the game result
            if count % 2 != 0:
                print("YOU LOST")
                print("BETTER LUCK NEXT TIME")
                #ending the game
                exit()
            else:
                print("YOU WON THE GAME")
                print("CONGRATULATIONS!!")
                #ending the game
                exit()
#printing a message if the input is out of range
else:
    print("OOPS!!")
    print("YOU ENTERED A NUMBER OUT OF RANGE")
    exit()

print()
#printing the output if the it is a tie
print("OOPS!!")
print("IT'S A TIE") 
