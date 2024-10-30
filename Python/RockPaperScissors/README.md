<h1>Description of the Rock-Paper-Scissors Program</h1>
    <p>This Python program allows users to engage in a classic game of Rock-Paper-Scissors against a computer opponent. The program features a user-friendly interface where players can choose their tool (rock, paper, or scissors) and see the outcome of each round. Here's a breakdown of its key functionalities:</p>
    
<h2>Key Functionalities:</h2>
    <ul>
        <li><strong>Gameplay Mechanics:</strong> The game accepts user input for the chosen tool, then randomly generates the computer's choice. It determines the outcome—win, loss, or draw—based on the standard rules of Rock-Paper-Scissors.</li>
        <li><strong>Multiple Rounds:</strong> Users can decide how many rounds they want to play. The program keeps track of the total wins, losses, and draws, providing a summary at the end of the session.</li>
        <li><strong>Input Validation:</strong> The program includes basic input validation, ensuring that users only enter valid choices (r for rock, p for paper, s for scissors). If the user enters an invalid option three times, the game will terminate to avoid confusion.</li>
        <li><strong>User Experience Enhancements:</strong> To enhance the user experience, the program incorporates pauses using the <code>sleep</code> command, creating a smoother flow of information between each round. This allows users to take in the results before moving on to the next round.</li>
    </ul>

<h2>How It Works:</h2>
    <ul>
        <li><strong>Function Definitions:</strong>
            <ul>
                <li><code>rps(p1, p2)</code>: Evaluates the result of a match between player input and computer choice.</li>
                <li><code>full(tool)</code>: Converts shorthand input to full names for better readability.</li>
                <li><code>players_input()</code>: Handles player input and computer choice, displaying the results.</li>
                <li><code>play(no_of_plays)</code>: Manages the overall game loop, counting wins, losses, draws, and invalid inputs.</li>
            </ul>
        </li>
    </ul>

<h2>Game Flow:</h2>
  <p>The program starts by prompting the player for the number of rounds to play.<br> 
    It enters a loop where it repeatedly asks for player input and computes results until the specified number of rounds is reached or too many invalid inputs are given.<br>
    After the gameplay, it prints a summary of the results, displaying the total wins, losses, and draws.</p>
