
import random

print("Ready for the Adventure of Janken :)")


while True:
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("ROCK, PAPER or SCISSOR? ").lower()

    print("Computer: ", computer)
    print("Player: ", player)

    if computer == player:

        print("TIE !!")

    elif player == "rock":

        if computer == "paper":
            print("You lose Idiot")

        if computer == "scissor":
            print("Wish I had a luck like you Winner !!")

    elif player == "paper":

        if computer == "scissor":
            print("You lose Idiot")

        if computer == "rock":
            print("Wish I had a luck like you Winner !!")

    elif player == "scissor":

        if computer == "rock":
            print("You lose Idiot")

        if computer == "scissor":
            print("Wish I had a luck like you Winner !!")

    play_again = input("If you're a champ, hit 'YES'. If you're a flop, hit 'NOPE!'\n").upper()

    if play_again != "YES":
        break

print("Catch you later, Champion!")
