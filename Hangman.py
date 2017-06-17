from __future__ import print_function
import numpy

welcome = ['Welcome to Hangman! A word will be chosen at random and',
'you must try to guess the word correctly letter by letter',
'before you run out of attempts. Good luck!'
               ]
print(welcome)

def printHangman(numberWrong):
    # Print the hangman
    print("  |------|")
    if numberWrong >= 1:
        print("  |      0")
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
    if numberWrong == 5:  # can't be > here so we get to the else :)
        print("  |     /")
    elif numberWrong >= 6:
        print("  |     / \\")
    else:
        print("  |")# don't print any legs
        print("-----")# print bottom of noose

def printBlanks(word, correctLetters):
    solved = True # Set solved equal to true (innocent until proven guilty)
    # Loop over each letter in the word
    for l in word:
        l = l.lower()  # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctLetters:  # Remove "False" and replace it with the appropriate condition
            print (l+ ' ', end = "")# If it is, print the letter and a space
        else:
            print ('_ ', end = "")# If it isn't, print an underscore and a space
            #Also, set solved equal to False
            solved = False#
    print()
    print()
    return solved

my_list = ["duketip", "intelligence", "umbrella", "pizza", "matthew", "chicken", "knife"]  # Define a list of words as options
correctLetters = [ ]
word = numpy.random.choice(my_list)
numberWrong = 0

# Define a variable to count the number of incorrect guesses

# Pick a random word to be used

while True:# Repeat forever, we'll use a break to get out
     # Print the Status of the Hangman
    print (Hangman(numberWrong)) # Print the word blanks and see if they solved it
    solved = printBlanks(word, correctLetters)
    break# Replace False with a function call
    if correctLetters == len(word):
        print('You win!')
        # no need to guess again

    user_input = 0# Define a variable to hold user input
# Loop until they give a letter

# Check if the letter is in the word
    if numberWrong >= 5:
        print("You Lose!")# Replace True with the correct condition
                    # If it's right, put it in the correct letters list and let them know it was right
    if solved:
      print(numberWrong)# # f it's wrong, increment the wrong count and let them know it was wrong

    user_input = ""
    while len(user_input) != 1:
        user_input = raw_input("Please enter a letter")
    if user_input in word:
        correctLetters.append(user_input)
    else:
        numberWrong = numberWrong
    print()
print ("The word was" + ' ' + word)

# Reveal what the word was














