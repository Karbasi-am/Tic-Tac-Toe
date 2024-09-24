from random import choice
from termcolor import colored
from os import name, system

def end_game():
    for i in board:
        if isinstance(i,int):
            return False
        else:
            return True

def print_board():
    board2 = ''
    x = 1
    for i in board:
        if x == 3 or x == 6 or x == 9:
            board2 += f'{i}\n'
        else:
            board2 += f'{i}  '    
        x += 1
    print(board2)

def board_changer(player,location:int):
    board.remove(location)
    board.insert(location - 1, player)

def computer_choice():
    frees = []
    for i in board:
        if type(i) == int:
            frees.append(i)   
    return choice(frees)
    
def check_win():
    for i in range(0,3,3):
        if board[i] == board[i + 1] == board[i + 2]:
            print(f"{board[i]} Won")
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            print(f"{board[i]} Won")
            return True
    if board[2] == board[4] == board[6]:
            print(f"{board[i]} Won")
            return True
    if board[0] == board[4] == board[8]:
            print(f"{board[i]} Won")
            return True
    return False


if name == 'nt':
    system('cls')
else: 
    system('clear')
user, computer = colored('X', 'red'), colored('O', 'blue')
board = list(range(1,10))
print(colored("You Play as", "yellow"), user, colored("\nComputer Plays as", "yellow"), computer)
print_board()
while check_win() == False:
    user_choice = int(input("Enter your Choice: "))
    board_changer(user, user_choice)
    board_changer(computer, computer_choice())
    print_board()
    if end_game == True:
        break
