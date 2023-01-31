import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r" or player_move == "rock":
    player_move = rock
elif player_move == "p" or player_move == "paper":
    player_move = paper
elif player_move == "s" or player_move == "scissors":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(Fore.LIGHTBLUE_EX + f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print(Fore.GREEN + "You win!")

elif player_move == computer_move:
    print(Fore.YELLOW + "Draw!")

else:
    print(Fore.RED + "You lose!")

play_again = input(Fore.GREEN + "Type [yes] to play Again or [no] to quit: ")

if play_again == "yes":
    exec(open("rock_paper_scissors.py").read())
else:
    print("Thank you for playing!")
