import pygame
from game import Game
from board import Board
from MCTS import MCTree, GameState
from randomFunctions import getPlayerMove, getNextPlayer, setBoard

testGame = Game()

#horizontalArray = [['__', '__', '__', '__', '__'], ['__', '__', '__', '__', '__'], ['__', '__', '__', '__', ' '], ['__', ' ', ' ', '__', ' '], ['__', ' ', '__', ' ', ' '], ['__', ' ', ' ', '__', ' ']]

#verticalArray = [['|', '|', '|', '|', '|', '|'], ['|', '|', '|', ' ', ' ', '|'], ['|', ' ', '|', '|', '|', '|'], ['|', '|', '|', ' ', '|', '|'], ['|', '|', '|', ' ', '|', '|']]

#squares = [['R', 'R', 'R', 'R', 'R'], ['R', 'R', ' ', ' ', ' '], [' ', ' ', ' ', 'B', ' '], ['R', ' ', ' ', ' ', ' '], ['B', ' ', ' ', ' ', ' ']]

#turn = "B"

#setBoard(horizontalArray, verticalArray, squares, turn, testGame.board)

testGame.start()

userPlayer = "R"

moveNum = 0


pygame.init()

def drawBoard(board, screen):
    screen.fill((200, 200, 200))

    for r in range(len(board.squares)):
        for c in range(len(board.squares[0])):
            if board.squares[r][c] == "R":
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((c * 90 + 20, r * 90 + 20, 90, 90)))
            if board.squares[r][c] == "B":
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((c * 90 + 20, r * 90 + 20, 90, 90)))

    for r in range(len(board.horizontalEdgesArray)):
        for c in range(len(board.horizontalEdgesArray[r])):
            if board.horizontalEdgesArray[r][c] != " ":
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((c*90 + 20, r*90+20, 90, 10)))


    for r in range(len(board.verticalEdgesArray)):
        for c in range(len(board.verticalEdgesArray[r])):
            if board.verticalEdgesArray[r][c] != " ":
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((c * 90 + 20, r * 90 + 20, 10, 90)))

    for r in range(12):
        for c in range(12):
            if not (r % 2 == 1 and c % 2 == 1):
                pygame.draw.circle(screen, (124, 124, 124), (r*45 + 25, c*45 + 25), 5)

    for rDot in range(6):
        for cDot in range(6):
            pygame.draw.circle(screen, (0, 0, 0), (rDot*90 + 25, cDot*90 + 25), 10)








screen = pygame.display.set_mode((500, 500))

more = True

keepGoing = True

while keepGoing:
    justMoved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keepGoing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if testGame.board.turn == userPlayer and more:
                try:
                    row = (position[1] - 20) // 45
                    col = (position[0] - 20) // 90
                    move = [row, col]
                    testGame.board = testGame.board.makeMove(move[0], move[1])
                    moveNum += 1
                    justMoved = True
                except:
                    pass
    if testGame.board.turn != userPlayer:
        if more and not justMoved:
            tree = MCTree(GameState(testGame.board))
            if moveNum < 40:
                move = tree.makeChoice(1000, moveNum)
            else:
                move = tree.makeChoice(4000, moveNum)
            testGame.board = move[0]
            if abs(move[1]) < 50:
                print("evaluation:", move[1])
            elif move[1] < -50:
                print("Uh oh... I think I'm gonna lose :(")
            else:
                print("GG's. Just concede now.")

            moveNum += 1

    print('')
    testGame.board.printBoard()

    if testGame.board.gameOver():
        print(testGame.board.getWinner() + ' has won!')
        more = False


    drawBoard(testGame.board, screen)
    pygame.display.update()