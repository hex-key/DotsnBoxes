from this import d


class Board:

    def __init__(self, board=None, turn="R"):

        if turn != "R":
            self.turn = turn
        else:
            self.turn = "R"

        self.horizontalEdgesArray = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "]
            ]

        self.verticalEdgesArray = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
            ]
        
        self.squares = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "]
        ]

        if board != None:

            for r in range(7):
                for c in range(6):
                    self.horizontalEdgesArray[r][c] = board.horizontalEdgesArray[r][c]
            
            for r in range(6):
                for c in range(7):
                    self.verticalEdgesArray[r][c] = board.verticalEdgesArray[r][c]
            
            for r in range(6):
                for c in range(6):
                    self.squares[r][c] = board.squares[r][c]
    
    def gameOver(self):
        for r in range(6):
            for c in range(6):
                if self.squares[r][c] == " ":
                    return False
        return True

    def getWinner(self):
        if self.gameOver():
            redCount = 0
            blueCount = 0

            for r in range(6):
                for c in range(6):
                    if self.squares[r][c] == "R":
                        redCount += 1
                    else:
                        blueCount += 1

            if redCount > blueCount:
                return "R"
            elif redCount == blueCount:
                return "T"
            else:
                return "B"
        else:
            return None       
    
    def makeMove(self, edgeRow, edgeCol):
        nextTurn = self.getNextTurn()
        if edgeRow % 2 == 0:
            self.horizontalEdgesArray[edgeRow//2][edgeCol] = "__"

            # Find the square above
            try: 
                topEdge = self.horizontalEdgesArray[edgeRow//2-1][edgeCol]
                rightEdge = self.verticalEdgesArray[edgeRow//2-1][edgeCol+1]
                leftEdge = self.verticalEdgesArray[edgeRow//2-1][edgeCol]

                if topEdge != " " and rightEdge != " " and leftEdge != " ":
                    self.squares[edgeRow//2-1][edgeCol] = self.turn
                    nextTurn = self.turn

            except:
                pass

            self.horizontalEdgesArray[edgeRow//2][edgeCol] = "__"

            # Find the square below
            try: 
                bottomEdge = self.horizontalEdgesArray[edgeRow//2+1][edgeCol]
                rightEdge = self.verticalEdgesArray[edgeRow//2][edgeCol+1]
                leftEdge = self.verticalEdgesArray[edgeRow//2][edgeCol]

                if bottomEdge != " " and rightEdge != " " and leftEdge != " ":
                    self.squares[edgeRow//2][edgeCol] = self.turn
                    nextTurn = self.turn
            except:
                pass

        
        else:
            self.verticalEdgesArray[(edgeRow-1)//2][edgeCol] = "|"

            # Find the square to the left
            try: 
                topEdge = self.horizontalEdgesArray[(edgeRow-1)//2][edgeCol-1]
                bottomEdge = self.horizontalEdgesArray[(edgeRow-1)//2+1][edgeCol-1]
                leftEdge = self.verticalEdgesArray[(edgeRow-1)//2][edgeCol-1]

                if topEdge != " " and bottomEdge != " " and leftEdge != " ":
                    self.squares[(edgeRow-1)//2][edgeCol-1] = self.turn
                    nextTurn = self.turn

            except:
                pass

            # Find the square to the right
            try: 
                topEdge = self.horizontalEdgesArray[(edgeRow-1)//2][edgeCol]
                bottomEdge = self.horizontalEdgesArray[(edgeRow-1)//2+1][edgeCol]
                rightEdge = self.verticalEdgesArray[(edgeRow-1)//2][edgeCol+1]

                if topEdge != " " and bottomEdge != " " and rightEdge != " ":
                    self.squares[(edgeRow-1)//2][edgeCol] = self.turn
                    nextTurn = self.turn
            except:
                pass
            
        return Board(self, nextTurn)
    
    def getNextTurn(self):
        if self.turn == "R":
            return "B"
        else:
            return "R"

    
    def getNextMoves(self):

        possibleMoves = []

        for hRow in range(7):
            for hCol in range(6):
                if self.horizontalEdgesArray[hRow][hCol] == " ":
                    possibleMoves.append([hRow*2, hCol])
        
        for vRow in range(6):
            for vCol in range(7):
                if self.verticalEdgesArray[vRow][vCol] == " ":
                    possibleMoves.append([vRow*2+1, vCol])

        possibleNextBoards = []

        for move in possibleMoves:
            newBoard = Board(self, self.turn)

            newBoard = newBoard.makeMove(move[0], move[1])

            possibleNextBoards.append(newBoard)


        return possibleNextBoards

    def printBoard(self):

        """
        .  .__.__.
           |  | B|
        .__.  .__.
        | B|  | R|
        .__.__.__.
        
        """
        for row in range(13):
            for col in range(13):
                if row % 2 == 0:
                    if col % 2 == 0:
                        print(".", end = "")
                    else:
                        if self.horizontalEdgesArray[(row)//2][(col-1)//2] != " ":
                            print("__", end = "")
                        else:
                            print("  ", end = "")
                    
                else:
                    #print(self.verticalEdgesArray)
                    if col % 2 == 0:
                        if self.verticalEdgesArray[(row-1)//2][(col)//2] != " ":
                            print("|", end = "")
                        else:
                            print(" ", end = "")
                    else:
                        print(self.squares[(row-1)//2][(col-1)//2], end = " ")
            print()

