from board import Board

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