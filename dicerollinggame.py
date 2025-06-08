"""
Dice Rolling Game

This script allows the user to roll two dice as many times as they want.
The user can choose to roll or exit the game.
"""

import random

while True:
    try:
        number=int(input("how many dices do you want to play with: "))
        if number < 1:
            print("please enter a positve number!:")
            continue
    except ValueError:
        print("Invalid input, please enter a number.")
        continue
        # Ask user to roll the dice
    choice = input("Roll the dice? (y/n): ").lower()
        # If user enters 'y', roll the dice
    if choice == 'y':
        for i in range(number):
            print(f"Die{i+1}: {random.randint(1,6)}")
            # Generate two random numbers between 1 and 6
            #die1 = random.randint(1, 6)
            #die2 = random.randint(1, 6)
           # print(f'{die1}')  # Print the results
        # If user enters 'n', exit the game
    elif choice == 'n':
            print("Thank you for participating")
            break
        # Handle invalid input
    else:
            print("Invalid input, try again")