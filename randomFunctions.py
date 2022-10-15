from board import Board
from game import Game
import random

def hasWon(board, player):

    winner = board.getWinner()
    if winner == player:
        return True
    
    else:
        return False

def getNextPlayer(player):
    if player == "R":
        return "B"
    else:
        return "R"

def simulate(board):
    simBoard = Board(board, board.turn)

    while not simBoard.gameOver():

        possibleMoves = []

        for hRow in range(6):
            for hCol in range(5):
                if simBoard.horizontalEdgesArray[hRow][hCol] == " ":
                    possibleMoves.append([hRow*2, hCol])
        
        for vRow in range(5):
            for vCol in range(6):
                if simBoard.verticalEdgesArray[vRow][vCol] == " ":
                    possibleMoves.append([vRow*2+1, vCol])
        
        chosenMove = random.randint(0, len(possibleMoves)-1)

        simBoard = simBoard.makeMove(possibleMoves[chosenMove][0], possibleMoves[chosenMove][1])

    winner = simBoard.getWinner()
    if winner == "R":
        return 50
    elif winner == "B":
        return -50
    else:
        return 0

def getPlayerMove():
    row = int(input("Which row? "))
    col = int(input("Which col? "))

    return [row, col]