# A program that plays Rock, Paper, Scissors with a user. The program will
# choose a random "number" and then the user will input a "number". Number will
# correspond with rock, paper, or scissors. The winner will be declared and all
# ties will result in a new match.
# 4-5-2019
# CTI-110-0003 P5HW2 - Rock, Paper, Scissors Game
# Clayton Zepeda
#


# Import random module
# Computer will secretly generate a choice.
# Prompt the user for input Rock, Paper, or Scissors.
# Display the winner and reset the game.

# import random
import random

def main():

# create a list of choices for PC to randomly choose from
    game_list = ['Rock', 'Paper', 'Scissors']
    
# PC makes a random choice from list.
    computer_choice = random.choice(game_list)
    
# Prompt user for choice
    print('Choose your weapon! Rock, Paper, or Scissors?\n')
    user_choice = input('Enter your choice of weapon!: ')
    
# Using nested if statements, determine a winner if computer picks 'Rock'.
    print('Computer picks',(computer_choice))
    print('\n')
    if computer_choice == 'Rock':
        if user_choice == 'Rock':
            print('Draw!\n')
            main()
        elif user_choice == 'Paper':
            print('Paper covers Rock, You win!')
        elif user_choice == 'Scissors':
            print('Rock crushes Scissors, You lose!')
        else:
            print("Let's go again!")
            main()
# Using nested if statements, determine a winner if computer picks 'Paper'.
    elif computer_choice == 'Paper':
        if user_choice == 'Paper':
            print('Draw!\n')
            main()
        elif user_choice == 'Rock':
            print('Paper covers Rock, You lose!')
        elif user_choice == 'Scissors':
            print('Scissors cuts Paper, You win!')
        else:
            print("Let's go again!")
            main()

# Using nested if statements, determine a winner if computer picks 'Scissors'.
    else:
        if computer_choice == 'Scissors':
            if user_choice == 'Scissors':
                print('Draw!\n')
                main()
        elif user_choice == 'Rock':
            print('Rock crushes Scissors, You win!')
        elif user_choice == 'Paper':
            print('Scissors cuts Paper, You lose!')
        else:
            print("Let's go again!")
            main()
main()

