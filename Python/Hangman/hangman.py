#Hangman
import random

words = ["word", "tackle", "brief","python","jaguar"]
word = words[random.randint(0,4)]
hidden_word = ([ '-' for letter in word])


def find_letters(hidden_word, word, letter, correctLetters):
    """
    Desc: This program finds the letter in the hidden word and displays it.
    args
    hidden_word: displayed with underscores (_) for unguessed letters and revealed letters in their correct positions. 
    word: the word to guess
    letter: User input for guessing a letter in the word
    correctLetters: set of letters user has guessed correctly
    Return: Boolean
    """
    if letter in word:
        # show guessed letters
        for i in range(0, len(word) -1):
            if word[i] == letter:
                hidden_word[i] = letter
            else:
                continue
        correctLetters.add(letter)
        return True
    else:
        return False


def play(word, hidden_word):
    print(word)
    wordLetters = set(word)
    usedLetters = set()
    correctLetters = set()

    chances = 3 
    letter = ""
    while chances != 0 and len(correctLetters) != len(wordLetters):
        print(f"{" ".join(hidden_word)}  := Used letters: {" ".join(usedLetters)}")
        letter = input("Enter a letter: ")
        #check if the letter has been used or not
        if letter in usedLetters:
            print("This letter has been used")
            chances -= 1
            print(f"You have {chances} chances left")
        else:
            usedLetters.add(letter)
            #check if the letter is in the word and display it
            isPresent = find_letters(hidden_word, word, letter, correctLetters)
            if not isPresent:
                print("Letter not in word")
                chances -= 1
                print(f"You have {chances} chances left")
        

        if len(correctLetters) == len(wordLetters):
            print(word)
            print("You win")
            

play(word, hidden_word)