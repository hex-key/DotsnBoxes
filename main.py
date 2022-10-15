from game import Game
from board import Board
from MCTS import MCTree, GameState
from randomFunctions import getPlayerMove, getNextPlayer

testGame = Game()
testGame.start()

userPlayer = "R"

while not testGame.board.gameOver():
    if testGame.board.turn == userPlayer:
        print(testGame.board.turn + " your go!")
        move = getPlayerMove()
        testGame.board = testGame.board.makeMove(move[0], move[1])
    else:
        tree = MCTree(GameState(testGame.board))
        move = tree.makeChoice(5000)
        testGame.board = move[0]
        if abs(move[1]) < 30:
            print("evaluation:", move[1])
        elif move[1] < 0:
            print("Uh oh... I think I'm gonna lose :(")
        else:
            print("GG's. Just concede now.")

    print('')
    testGame.board.printBoard()

    if testGame.board.gameOver():
        print(testGame.board.getWinner() + ' has won!')
        break