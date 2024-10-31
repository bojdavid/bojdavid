<h1>Hangman Game in Python</h1>

  <p>This Python code is a simple implementation of the Hangman game, where a player has a limited number of chances to guess a randomly chosen word. Each guessed letter that appears in the word is revealed in its correct position, while incorrect guesses reduce the player’s chances.</p>

  <h2>Game Steps</h2>
  <ul>
    <li><strong>Choosing a Word</strong>: The program selects a random word from a predefined list.</li>
    <li><strong>Hidden Word Display</strong>: The word is initially hidden with hyphens (<code>-</code>), which are replaced by correctly guessed letters.</li>
    <li><strong>Tracking Guesses</strong>: The program keeps track of correct and used letters. Each guess is checked:
      <ul>
        <li>If the letter is in the word, it is revealed in the correct position.</li>
        <li>If the letter is not in the word or has already been guessed, the player loses one chance.</li>
      </ul>
    </li>
    <li><strong>Win or Lose</strong>: The player wins if they guess all letters before running out of chances; otherwise, they lose.</li>
  </ul>
