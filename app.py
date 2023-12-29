# create a cli minigame of rock paper scissors
# the game should ask the user to pick rock paper or scissors
# the computer will then pick rock paper or scissors
# the game will then output who won
# the game will track how many times the user won and how many times the computer won
# the game will track how many rounds the user and computer played
# the game will then ask if the user wants to play again
# the game will continue until the user says no
# the game will output how many times the user won and how many times the computer won
# the game will output who won the game
# the game must handle user inputs, putting them in lowercase and informing the user if they did not input rock paper or scissors

import random
import time

def main():
    # initialize variables
    user_wins = 0
    computer_wins = 0
    rounds = 0
    user_choice = ""
    computer_choice = ""
    play_again = "y"

    # loop until the user wants to stop playing
    while play_again == "y":
        # get user input
        user_choice = input("Rock, Paper, or Scissors? ").lower()
        # check for valid input
        while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            print("Invalid input. Please try again.")
            user_choice = input("Rock, Paper, or Scissors? ").lower()
        # get computer input
        computer_choice = random.randint(1, 3)
        # convert computer input to string
        if computer_choice == 1:
            computer_choice = "rock"
        elif computer_choice == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"
        # print choices
        print("You chose " + user_choice + ".")
        time.sleep(1)
        print("The computer chose " + computer_choice + ".")
        time.sleep(1)
        # determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "paper":
            print("The computer wins!")
            computer_wins += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            user_wins += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            user_wins += 1
        elif user_choice == "paper" and computer_choice == "scissors":
            print("The computer wins!")
            computer_wins += 1
        elif user_choice == "scissors" and computer_choice == "rock":
            print("The computer wins!")
            computer_wins += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            user_wins += 1
        # increment rounds
        rounds += 1
        # ask user if they want to play again
        play_again = input("Play again? (y/n) ").lower()
        # check for valid input
        while play_again != "y" and play_again != "n":
            print("Invalid input. Please try again.")
            play_again = input("Play again? (y/n) ").lower()
    # print results
    print("You won " + str(user_wins) + " times.")
    print("The computer won " + str(computer_wins) + " times.")
    if user_wins > computer_wins:
        print("You won the game!")
    elif user_wins < computer_wins:
        print("The computer won the game!")
    else:
        print("The game was a tie!")

if __name__ == "__main__":
    main()

# Path: app.py
# create a cli minigame of rock paper scissors
# the game should ask the user to pick rock paper or scissors
    
    