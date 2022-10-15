from game import Game
from board import Board
from MCTS import MCTree, GameState
from randomFunctions import getPlayerMove, getNextPlayer, setBoard

testGame = Game()

horizontalArray = [['__', '__', '__', ' ', ' '], ['__', '__', ' ', ' ', ' '], ['__', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '__', '__', ' '], [' ', ' ', ' ', '__', ' ']]

verticalArray = [['|', '|', '|', ' ', ' ', '|'], ['|', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '|', ' '], [' ', ' ', '|', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]

squares = [['R', 'R', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

turn = "R"

#setBoard(horizontalArray, verticalArray, squares, turn, testGame.board)

testGame.start()

userPlayer = "R"

moveNum = 0

while not testGame.board.gameOver():
    moveNum += 1
    if testGame.board.turn == userPlayer:
        print(testGame.board.turn + " your go!")
        move = getPlayerMove()
        testGame.board = testGame.board.makeMove(move[0], move[1])
    else:
        tree = MCTree(GameState(testGame.board))
        move = tree.makeChoice(1000, moveNum)
        testGame.board = move[0]
        if abs(move[1]) < 50:
            print("evaluation:", move[1])
        elif move[1] < -50:
            print("Uh oh... I think I'm gonna lose :(")
        else:
            print("GG's. Just concede now.")

    print('')
    testGame.board.printBoard()

    if testGame.board.gameOver():
        print(testGame.board.getWinner() + ' has won!')
        break