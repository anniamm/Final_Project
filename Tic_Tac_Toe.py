# Tic Tac Toe code

import random

class Game_Board:
    def __init__(self):
        self.board = []
        for i in range(10):
            self.board += [' ']
    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def makeMove(self , letter, move):
        self.board[move] = letter

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove1(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(self.board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def getPlayerMove2(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(self.board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(self.board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(self.board, i):
                return False
        return True

    def isWinner(self, le):
        bo = self.board
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


class PlayerMoves:

    def inputPlayerLetter(self):

        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'player2'

class Winner:
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')



print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    gb = Game_Board()
    dec = PlayerMoves()
    win = Winner()
    playerletter1, playerletter2 = dec.inputPlayerLetter()
    PlayerLetters = {'player1':playerletter1, 'player2': playerletter2}
    currentPlayer = dec.whoGoesFirst()
    print('The ' + currentPlayer + ' will go first.')
    gameIsPlaying = True



    while gameIsPlaying:

        # Player's turn.
        gb.drawBoard()
        move = gb.getPlayerMove()
        gb.makeMove(PlayerLetters[currentPlayer], move)

        if gb.isWinner( playerletter1):
            gb.drawBoard()
            print('Hooray! You have won the game!')
            gameIsPlaying = False
        else:
            if gb.isBoardFull():
                gb.drawBoard()
                print('The game is a tie!')
                gameIsPlaying = False

        if 'player1' == currentPlayer:
            currentPlayer = 'player2'

        else:
            currentPlayer = 'player1'




    if not playAgain():
        break