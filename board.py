class Board:

    def __init__(self, board=None, turn="R"):

        if self.turn != "R":
            self.turn = turn

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
                    self.verticalEdgesArray[r][c] = board.squares[r][c]
    
    def gameOver(self):
        for r in range(6):
            for c in range(6):
                if board[r][c] == " ":
                    return False
        return True

            

        

