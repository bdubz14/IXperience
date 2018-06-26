# -*- coding: utf-8 -*-
"""

Ejercicio. Tic-tac-toe

We are going to build a program that allows us to play tic-tac-toe on the terminal


In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la 
izquerda, podemos acceder haciendo tablero[[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2
"""

import sys

def parse_arguments():
    arguments = sys.argv[1:]
    return arguments

def test(name):
    print('Hello {}'.format(name))

def game():
    cont = True
    player = 1
    turns = 1
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    print('Let us play Tic-Tac-Toe!')
    while cont and turns < 10:
        print(str(board[0]) + '\n' + str(board[1]) + '\n' + str(board[2]))
        coordinates = move(player)
        while board[int(coordinates[0])][int(coordinates[1])] != " ":
           coordinates = input('That spot is already filled! Try again: ')
        if player == 1:
            board[int(coordinates[0])][int(coordinates[1])] = 'X'
            turns += 1
            player = 2
        else:
            board[int(coordinates[0])][int(coordinates[1])] = 'O'
            turns += 1
            player = 1
        cont = check(board)
    print(str(board[0]) + '\n' + str(board[1]) + '\n' + str(board[2]))
    if turns == 10:
        print('Draw!')
    else:
        if player == 1:
            print('Player 2 wins!')
        else:
            print('Player 1 wins!')
        

def move(player):
    coordinates = input('Player ' + str(player) + ', what is your move? Enter row then column with no space: ')
    return(coordinates)

def check(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ' ':
        return(False)
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != ' ':
        return(False)
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != ' ':
        return(False)
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ':
        return(False)
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ':
        return(False)
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' ':
        return(False)
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return(False)
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != ' ':
        return(False)
    else:
        return(True)

if __name__ == "__main__":
    game()
