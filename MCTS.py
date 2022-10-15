import numpy as np
from randomFunctions import hasWon, getNextPlayer, simulate
from board import Board

userPlayer = "R"


# Things a game state needs:
# - the literal game state (board)
# - whose turn it is
# - pointer to the parent (if it exists)
# - pointers to the children (if they exist)
# - a total score
# - a counter to keep track of the number of visits
# - a method to calculate UCBI
# - a method that expands a node
# - a method that finds highestUCBI

# note: what is UCBI? It's a way to balance between exploration and exploitation.
# Exploitation side is the average value (self.total/self.visits)
# Exploration side is 2 * √(ln(visits to parent)/visits to child)
# UCBI is sum of Exploitation value + Exploration value
class GameState:

    def __init__(self, board):
        self.board = board
        self.total = 0
        self.visits = 0
        self.player = self.board.turn

        self.parent = None
        self.children = []
        self.leaf = False

        if self.board.gameOver():
            winner = self.board.getWinner()
            self.leaf = True

            if winner == userPlayer:
                self.total = -50
                self.visits = 0
            elif winner == "B":
                self.total = 50
                self.vivists = 0

            else:
                self.total = 0
                self.visits = 0

    def setParent(self, parentState):
        self.parent = parentState
        self.player = getNextPlayer(parentState.player)
        parentState.addChild(self)
        if self.board.gameOver():
            winner = self.board.getWinner()
            self.leaf = True

            if winner == userPlayer:
                self.total = -50
                self.visits = 0
            elif winner == "B":
                self.total = 50
                self.vivists = 0

            else:
                self.total = 0
                self.visits = 0

    def addChild(self, childState):
        self.children.append(childState)

    def roll(self):
        if self.leaf:
            self.visits = -1
            return self.total
        return simulate(self.board)

    def addToTotal(self, newValue):
        self.total += newValue

        # now we have to update the parent as well
        # to do this, we'll use a bit of recursion!

        # base case:
        if self.parent == None:
            return
        # recursive step:
        else:
            self.parent.addToTotal(newValue)

    def addVisit(self):
        self.visits += 1

        # same as above
        # base case:
        if self.parent == None:
            return
        # recursive step:
        else:
            self.parent.addVisit()

    def calculateUCBI(self):

        if self.visits == np.Infinity:
            return np.Infinity

        # Formula:
        # average value + 10*√(ln(visits to parent)/visits to child)

        # THINGS THAT CAN BE 0
        # - self.visits -> return infinity because we have a fully unexplored branch
        # - self.parent -> CANNOT BE NONE because then this would never get called!
        # - self.total -> doesn't cause 0 division errors so we don't care

        if self.visits == 0:
            if self.player != userPlayer:
                return -np.Infinity
            return np.Infinity

        else:
            try:
                exploitationValue = self.total / self.visits
            except:
                exploitationValue = self.total // (self.visits)

            # NOTE: np.log is actually ln(), np.log10 is standard log()
            explorationValue = 20 * np.sqrt(np.log(self.parent.visits) / self.visits)

            if self.player != userPlayer:
                explorationValue *= -1

            try:
                return exploitationValue + explorationValue
            except:
                return 1 * 10 ** 200

    def getChildrenUCBIs(self):
        childScores = []

        for child in self.children:
            childScores.append(child.calculateUCBI())

        return childScores

    def findHighestUCBILeaf(self):

        # base case:
        if self.visits == 0 and self.parent != None:
            return self

        # recursive step(s):
        if self.children == []:
            self.expand()
            try:
                return self.children[0]
            except:
                return self

        else:
            UCBIs = self.getChildrenUCBIs()
            favoriteChild = 0

            if self.player != userPlayer:
                max = UCBIs[0]

                for childNum in range(len(UCBIs)):
                    if UCBIs[childNum] > max:
                        favoriteChild = childNum
                        max = UCBIs[childNum]

            else:
                min = UCBIs[0]

                for childNum in range(len(UCBIs)):
                    if UCBIs[childNum] < min:
                        favoriteChild = childNum
                        min = UCBIs[childNum]

            return self.children[favoriteChild].findHighestUCBILeaf()

    def expand(self):
        nextMoves = self.board.getNextMoves()

        for nextState in nextMoves:
            newState = GameState(Board(nextState, nextState.turn))
            newState.setParent(self)


# Things a MCTree needs:
# - root node -> this will point to all the other nodes
# - iterate() function that updates the values
# - makeChoice(x) function that iterates x times and picks out the best branch

# note: to write this, we need to assume that a few game-specific functions exist

class MCTree:

    def __init__(self, start):

        # note: this root is likely going to be a part of a different tree. So we can't just reuse it – we need to reset the total and visits
        self.root = start  # GameState(start.board, start.player)
        self.root.expand()

        """print("ROOT")
        printBoard(self.root.board)"""

    def iterate(self):
        leafToUpdate = self.root.findHighestUCBILeaf()

        score = leafToUpdate.roll()

        leafToUpdate.addToTotal(score)
        leafToUpdate.addVisit()

    def makeChoice(self, iterations, moveNum):
        for iteration in range(iterations):
            self.iterate()

        childScores = []
        rawScores = []

        for child in self.root.children:
            try:

                twoDeep = child.board.getNextMoves()

                if child.board.turn == "B":
                    minScore = [25, 0]
                    for state in twoDeep:
                        score = state.score()
                        if score[0] - score[1] < minScore[0] - minScore[1]:
                            minScore = score

                    score = minScore

                else:
                    maxScore = [0, 25]
                    for state in twoDeep:
                        score = state.score()
                        if score[0] - score[1] > maxScore[0] - maxScore[1]:
                            maxScore = score

                    score = maxScore

                rawScores.append(score[1] - score[0])
                childScores.append(child.total / child.visits)
            except:
                print("BADBADBADBADBAD")
                ready = input()
                childScores.append(child.total)

        approved = 0
        try:

            legalMoves = []
            for i in range(len(childScores)):
                legalMoves.append(i)

            if moveNum < 300:
                max = rawScores[0]
                legalMoves = []

                for i in range(len(rawScores)):
                    if rawScores[i] == max:
                        legalMoves.append(i)
                    elif rawScores[i] > max:
                        legalMoves = [i]
                        max = rawScores[i]

            max = childScores[0]

            for item in range(len(childScores)):
                if childScores[item] > max and item in legalMoves:
                    approved = item
                    max = childScores[item]
            # print(approved)
            return [self.root.children[approved].board, max]

        except:
            # print("except")
            return [self.root.children[0].board, 50]

