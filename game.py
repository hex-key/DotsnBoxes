from board import Board

class Game:

    def __init__(self):
        self.board = Board()
    
    def start(self):
        print("WOOOO PLAY SOME DOTS AND BOXES")
        self.board.printBoard()
        print()
        print()

    def prompt(self):
        if self.board.turn == "R":
            print("Red's Turn!")
        else:
            print("Blue's Turn!")
        
        row = int(input("row? "))
        col = int(input("col? "))

        return [row, col]
    
    def iterate(self):
        move = self.prompt()

        self.board = self.board.makeMove(move[0], move[1])
        #print(self.board.verticalEdgesArray[0])
        print()
        print()
        self.board.printBoard()

    def gameOver(self):
        return self.board.gameOver()