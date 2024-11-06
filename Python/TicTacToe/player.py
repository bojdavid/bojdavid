import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        # we want players to get thier next move during a game
        pass

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        #get a random valid spot for our next move 
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter +'\'s turn. Input move (0-8): ')
            """
                check if value is correct by trying to cast it to an integer
                and if its not, then we say it is invalid.
                If the spot is not available on the board, we say it is invalid
            """
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except:
                print("Invalid square, Try again.")
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose a square
        else:
            #get the square based of the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X" 

        #first, we want to check if the previous move is a winner
        #this is our base case
        if state.currentWinner == other_player:
            # we return position and score because we need to keep track of the score for minmax to work
            return {
                "position": None,
                "score" : 1 * (state.no_empty_squares() + 1) if other_player == max_player else -1 * (state.no_empty_squares() + 1)
            }
        
        elif not state.empty_squares():
            return {"position": None, "score": 0}
        
        #main algorithm
        if player == max_player:
            best = {"position": None, "score": -math.inf } #each score should be maximised
        else:
            best = {"position": None, "score": math.inf } #each score should be minimised

        for possible_move in state.available_moves():
            #step1: make a move, try that spot
            state.make_move(possible_move, player)

            #step2: recurse using minimax to simulate a game after making that move
            sim_score =self.minimax(state, other_player) # alternate players
            
            #step3: undo the move
            state.board[possible_move] = ' '
            state.currentWinner = None
            sim_score['position'] = possible_move #otherwise this will get messed up from the recurssion
            
            #step4: update the dictionary if neccessary (if score beats current best score)
            #maximise the max player, minimise the other player
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best["score"]:
                    best = sim_score 
        return best      


        

