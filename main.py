from game import Game
from board import Board

testGame = Game()
testGame.start()

while not testGame.gameOver():
    testGame.iterate()

