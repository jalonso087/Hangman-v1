#Javier Alonso
#Attempt 2
#01/11/2024

import random # for randomizing word choice

print("**Hangman**") # print game title

words = ['arguable', 'appreciative', 'universal', 'language'] # create list of multiple words
chosen_word = random.choice(words) # choose a random word from the words list
correct = 0 # store integer for number of correct guesses
incorrect = 0 # store integer for number of incorrect guesses
board_state = [] # create a list to store an underscore per letter into board state to use later
user_guess = '' # store user's current guess
all_guesses = [] # store list that contains all of user's guesses
counter = 0 # counter for incrementing guess list
winner = False # used for while loop to keep game running while there is no winner

#display board
def board(guess):
    for letter in chosen_word: # iterate through each letter in the chosen word
        if letter in guess: # if the chosen_word's letter is in the user's guess 
            print (letter, end=' ') # print the letter and continue on the same line
        else: # if the chosen_word's letter is not in the user's guess
            print("_", end=" ") # print an underscore for each letter
        
#ask user for guess
def guess():
    global correct
    global incorrect
    global all_guesses # necessary to make sure changes to the variable persist outside the function
    global user_guess # necessary to make sure changes to the variable persist outside the function
    user_guess = input("\nEnter a letter: ") # ask the user to enter a guess and assign it to a variable
    print("\n") # used to create separation for better visibility
    if user_guess in all_guesses: # if the user is choosing a repeated letter
        print("\nYou already tried that letter. Try another.\n") # let the user know they already used that letter before
        user_guess = input("\nEnter a letter: ") # ask the user to enter a guess and assign it to a variable
        print("\n") # used to create separation for better visibility
    else: # when user does not repeat a letter
        all_guesses += user_guess # assign the users guess to the list  of all user's guesses
    if user_guess in chosen_word: # if the user chose a letter that is in the chosen word variable
        correct += 1 # increment the user's correct guesses by 1. this is used to check for a win
    else: # if the user is not correct then it stands to reason that they must be incorrect
        incorrect += 1 # increment the users incorrect guesses by 1 to check against the total number of available incorrect guesses
    return all_guesses # to bring all guesses variable into the board function for use

#check winner
def check_win():
    if correct == len(chosen_word): # if the number of correct guesses is the same as the length of the chosen word
        print("You win!") # tell user they won
        exit() # exit program
    elif incorrect == 6: # if the number of incorrect guesses is 6
        print("You lose.")  # let the user know they lost
        exit() # exit program
        
    

# call functions
while not winner: # continue to play the game while there is no winner or loser
    board(guess()) # call board function with the user's guess as an argument
    print(f"\nYou have {incorrect}/6 incorrect guesses.\n") # display the loss scenario to the user
    check_win() # check if the user has won or lost



