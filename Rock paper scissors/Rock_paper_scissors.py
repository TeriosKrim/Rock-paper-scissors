import random

print("Winning rules of the game ROCK PAPER SCISSORS are:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

while True:
    print("Enter your choice:\n1 - Rock\n2 - Paper\n3 - Scissors")
    choice = int(input("Your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid choice (1-3): "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = "Scissors"

    print("You chose:", choice_name)
    print("Now it's the computer's turn...")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    print("The computer chose:", comp_choice_name)

    if choice == comp_choice:
        print("It's a tie!\n")
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("Paper wins!\n")
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Rock wins!\n")
        result = "Rock"
    else:
        print("Scissors wins!\n")
        result = "Scissors"

    if result == 'DRAW':
        print("It's a tie!")
    elif result == choice_name:
        print("You win!")
    else:
        print("The computer wins!")

    print("Do you want to play again? (Enter 'Y' to play again, 'N' to quit)")
    play_again = input().lower()

    if play_again != 'y':
        break

print("Thanks for playing!")
