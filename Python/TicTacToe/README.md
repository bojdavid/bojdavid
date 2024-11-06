<h1>Tic Tac Toe Game Documentation</h1>
    <h2>Overview</h2>
    <p>This is a Python implementation of Tic Tac Toe with different player types: 
      <ol>
      <li>
          <strong>HumanPlayer:</strong> Gets input from the user.
      </li>
      <li>
          <strong>RandomComputer:</strong> Selects moves randomly.
      </li>
      <li>
        <strong>GeniusComputerPlayer:</strong> Uses the Minimax algorithm for optimal moves ensuring the computer never loses.  
      </li>
    </ol>
    <p>The game board is a 3x3 grid represented as a list, and the game continues until a player wins or the board is filled.</p>

  <h2>Modules</h2>
    <h3>player.py</h3>
    <p>Defines player types and their strategies.</p>

  <ul>
        <li><strong>Player Class</strong>
            <ul>
                <li><code>__init__(self, letter)</code>: Initializes the player with 'X' or 'O'.</li>
                <li><code>get_move(self, game)</code>: Abstract method to get the next move.</li>
            </ul>
        </li>
        <li><strong>RandomComputer Class</strong> (inherits from Player)
            <ul>
                <li><code>get_move(self, game)</code>: Chooses a random valid move.</li>
            </ul>
        </li>
        <li><strong>HumanPlayer Class</strong> (inherits from Player)
            <ul>
                <li><code>get_move(self, game)</code>: Prompts the user for input and validates the move.</li>
            </ul>
        </li>
        <li><strong>GeniusComputerPlayer Class</strong> (inherits from Player)
            <ul>
                <li><code>get_move(self, game)</code>: Uses the Minimax algorithm for optimal moves.</li>
                <li><code>minimax(self, state, player)</code>: Implements Minimax to calculate the best move.</li>
            </ul>
        </li>
    </ul>

  <h3>game.py</h3>
    <p>Handles the game mechanics and board setup.</p>

  <ul>
        <li><strong>TicTacToe Class</strong>
            <ul>
                <li><code>__init__(self)</code>: Initializes a 3x3 board and tracks the current winner.</li>
                <li><code>print_board(self)</code>: Displays the current board.</li>
                <li><code>print_board_nums()</code>: Static method to show position numbers on the board.</li>
                <li><code>available_moves(self)</code>: Returns a list of available moves.</li>
                <li><code>empty_squares(self)</code>: Checks if there are any empty squares.</li>
                <li><code>no_empty_squares(self)</code>: Counts empty squares.</li>
                <li><code>make_move(self, square, letter)</code>: Makes a move if the square is empty and updates the winner.</li>
                <li><code>winner(self, square, letter)</code>: Checks rows, columns, and diagonals for a win.</li>
            </ul>
        </li>
        <li><strong>play(game, x_player, o_player, print_game=True)</strong>: Main function to play the game.</li>
    </ul>

  <h2>Example Usage</h2>
    <pre><code>
from player import HumanPlayer, GeniusComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x = HumanPlayer("X")
    o = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x, o)
    </code></pre>


<h2>Game Flow</h2>

  <h3>Setup:</h3>
    <ul>
        <li>The board is represented by a 3x3 list with nine positions (0 through 8).</li>
        <li>Player "X" always goes first, and players take turns marking available spots on the board.</li>
    </ul>

  <h3>Players:</h3>
    <ul>
        <li><strong>HumanPlayer:</strong> Prompts the user to enter their move, which should be a valid position number.</li>
        <li><strong>RandomComputer:</strong> Chooses an empty square randomly.</li>
        <li><strong>GeniusComputerPlayer:</strong> Selects moves based on the Minimax algorithm, aiming to maximize its chance of winning or, if not possible, to draw.</li>
    </ul>

  <h3>Playing the Game:</h3>
    <ul>
        <li>On each turn, the current player selects an available move.</li>
        <li>The game checks whether the chosen square is valid and, if so, places the player’s symbol (X or O) on that square.</li>
        <li>The board is then displayed to show the latest move.</li>
    </ul>

  <h3>Determining a Win or Draw:</h3>
    <ul>
        <li>After every move, the game checks if there is a winner:</li>
        <ul>
            <li><strong>Row check:</strong> Three of the same symbols in a row indicate a win.</li>
            <li><strong>Column check:</strong> Three of the same symbols in a column indicate a win.</li>
            <li><strong>Diagonal check:</strong> Three of the same symbols along a diagonal indicate a win.</li>
        </ul>
        <li>If a player achieves any of these, the game declares that player as the winner.</li>
        <li>If there are no remaining moves and no winner, the game ends in a tie.</li>
    </ul>

  <h3>End of Game:</h3>
    <ul>
        <li>The game terminates either when a player wins or when all squares are filled without a winner, resulting in a draw.</li>
        <li>A message is displayed indicating the result: either a win for "X" or "O" or a tie.</li>
    </ul>

   <h2>Winning Logic</h2>
    <p>The game uses a method called <code>winner</code> in the <code>TicTacToe</code> class to check for winning conditions after every move. This method verifies:</p>
    <ul>
        <li><strong>Rows:</strong> If all three squares in any row contain the same symbol.</li>
        <li><strong>Columns:</strong> If all three squares in any column contain the same symbol.</li>
        <li><strong>Diagonals:</strong> If all three squares in either diagonal contain the same symbol.</li>
    </ul>
    <p>This approach ensures that the game quickly identifies any winning combination, allowing it to end as soon as a player has won. If no player meets these conditions and no empty squares are left, the game concludes with a draw.</p>
