#Rock Paper Scissors
import random
from time import sleep

print("Rock Paper Scissors")


def rps(p1, p2):
    """
    desc := checks if the player wins, loses, or draws in a game of rock paper scissors
    Accept two inputs
    p1 := players input 
    p2 := randomized computer input
    returns a String 
    """

    if (p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r"):
        return "win"
    elif (p1 == "r" and p2 == "p") or (p1 == "s" and p2 == "r") or (p1 == "p" and p2 == "s"):
        return "lose"
    elif (p1 == "r" and p2 == "r") or (p1 == "s" and p2 == "s") or (p1 == "p" and p2 == "p"):
        return "draw"
    else:
        return "Invalid"
    

def full(tool):
    """
    Desc := converts short form of player input to full form
    accepts player input
    """
    if tool == "r":
        return "rock"
    elif tool == "p":
        return "paper"
    elif tool == "s":
        return "scissors"
    else:
        return tool

def players_input():
    """
    Desc := Prompts player for input
    return string
    """
    p1 = input("choose Your tool: ")
    tools = ["r", "p", "s"]
    p2 = tools[random.randint(0,2)]
    sleep(0.5)
    print(f"You chose {full(p1)} \nPlayer2 chose {full(p2)}")
    return (rps(p1, p2))

def play(no_of_plays):
    """
    Desc := allows multiple plays while keeping track of the no of outcomes
    args := no_of_plays
    no_of_plays := number of plays
    """
    win = 0
    loss = 0
    draws = 0
    count = 0
    invalid = 0
    while count < no_of_plays:
        outcome = players_input()
        if outcome == "Invalid":
            print("Your Input is Invalid \nr := rock \np := paper \ns := scissors\n")
            invalid += 1
        else:
            if outcome == "win":
                win += 1
            elif outcome == "lose":
                loss += 1
            else:
                draws += 1
            sleep(0.5)
            print(outcome)
            count += 1
            print(f"You have {no_of_plays - count} plays left\n")

        if invalid == 3:
            print("Too many invalid inputs.")
            break
    sleep(0.5)
    print(f"Wins = {win} \nLoss = {loss} \nDraws = {draws}")




no_of_plays = int(input("How many times do you want to play? "))
play(no_of_plays)
