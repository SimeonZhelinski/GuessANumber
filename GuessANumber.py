import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid Input. Try again... ")
        continue
    player_digit = int(player_input)
    if player_digit > 100 or player_digit < 1:
        continue
    if player_digit == computer_number:
        print("You guessed it!")
        print()
        another_game = input("Do you want to play again ? [y]es / [n]o: ")
        if another_game == "y":
            continue
        else:
            print("Thanks for playing !")
            break
    elif player_digit > computer_number:
        print("Too High!")
    elif player_digit < computer_number:
        print("Too Low!")
        # colors
        # new code ...
