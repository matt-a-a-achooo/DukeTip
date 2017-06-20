from __future__ import print_function
import array


def printHangman(numberWrong):
    # Prints the hangman
    print("  |------|")
    if numberWrong >= 1:
        print("  |     ( )")
    else:
        print("  |")
    if numberWrong >= 2:
        print("  |      |")
    else:
        print("  |")
    if numberWrong >= 3:
        print("  |     /|\\")
    else:
        print("  |")
    if numberWrong >= 4:
        print("  |      |")
    else:
        print("  |")
    if numberWrong == 5:  # can't be > here so we get to the else :) - Loren
        print("  |     /")
    elif numberWrong >= 6:
        print("  |     / \\")
    else:
        print("  |")# don't print any legs - Loren
        print("-----")# print bottom of noose - Loren


def printBlanks(word, correctLetters):
    solved = True# Set solved equal to true (innocent until proven guilty) - Loren
    # Loop over each letter in the word - Loren
    for l in word:
        l = l.lower() #lowercase

        if l in correctLetters: #checks if letter is correct
            print(l + " ", end = "")# prints letter and a space if correct
        else:

            print ("_ ",end = "") #print _ if not
            solved = False
    print()
    print()
    return solved

my_list = ["tiger", "noodle", "chicken", "matthew", "duketip", "intelligent", "pizza", "croissant", "coding", "python", "knack", "sacrilegious", "eczema", "rhythm", "ecstasy", "pronunciation", "history", "neuroscience", "asian", "spider", "pirate", "mouse", "notebook"]# Define a list of words as options
correctLetters = [ ] #makes a list for the correctLetters
numberWrong = 0 # counts number of incorrect guesses


word = array.random.choice(my_list) #pciks a random word from my_list
# Repeat forever, we'll use a break to get out
while True:
    # Print the Status of the Hangman
    printHangman(numberWrong)
    # Print the word blanks and see if they solved it
    solved = printBlanks(word, correctLetters)  # Replace False with a function call

    if numberWrong >= 6:
        print ("OOOOOOOOOO YOU LOST LOL")# Catch Death (Exit loop if they got 6 or more wrong)
        break

    if solved:
        print('Congratulations, you have won!')
        break  # no need to guess again

    user_input = ""
    while len(user_input) != 1:
        user_input = raw_input("Please enter a letter:")#makes a varibale for users input
    # Loop


    if user_input in word:  # checks if user_input is in word
        correctLetters.append(user_input)# If it's right, it puts it in the correct_Letters list and let them know it was right
    else:
        numberWrong = numberWrong + 1# If it's wrong, increment the wrong count and let them know it was wrong - Loren
    print()

print ("The word was " + word)# Reveals word