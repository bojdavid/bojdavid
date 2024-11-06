from player import HumanPlayer, RandomComputer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [ " " for _ in range(9)] #using a single list to represent a 3x3 bored
        self.currentWinner = None #keep track of the current winner
         
    def print_board(self):
        for i in range(3):
            row = self.board[(i * 3) : ((i + 1) * 3)]
            print("|" + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        #tells us what number corresponds to what box 
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("|" + " | ".join(row) + " |")

    def available_moves(self):
        # returns []
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)

        return moves
    
    def empty_squares(self):
        return " " in self.board
    
    def no_empty_squares(self):
        return self.board.count(" ") #counts the number of spaces in the board

    def make_move(self, square, letter):
        #if the move is valid then assign the square to letter and return True, else False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self,square, letter):
        # wins if 3 forms a straight line
        
        #check rows
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #the only moves possible to win with a diagonal are even numbers (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all fails, return false
        return False
        

    





def play(game, x_player, o_player, print_game = True):
    #Returns the winner of the game or non for a tie
    if print_game:
        game.print_board_nums()
    
    letter = "X" #starting letter
    """
        Iterate while the game still has empty squares
        we don't have to worry about winner because we will just return that when we break the loop
    """

    while game.empty_squares():
        #get move from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #making a move
        if game.make_move(square, letter):
            if print_game:
                print(f" Letter {letter} makes a move to square {square}")
                game.print_board()
                print(" ") #Empty line

            if game.currentWinner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
        
            #alternate letters 
            letter = "O" if letter == "X" else "X"
    
    if print_game:
        print("It's a tie")
    

"""b = [[j for j in range(i * 3, (i + 1) * 3)]for i in range(3)]

a = [i for i in range(9)]
num = 8
num_ind = num // 3
c = a[(num_ind * 3) : (num_ind + 1) * 3]

print(c)
"""

if __name__ == '__main__':
    x = HumanPlayer("X")
    o = GeniusComputerPlayer("O")

    t = TicTacToe()
    play(t, x, o)