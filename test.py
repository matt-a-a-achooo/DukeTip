
welcome = ['Welcome to Hangman! A word will be chosen at random and',
'you must try to guess the word correctly letter by letter',
'before you run out of attempts. Good luck!'
               ]
print welcome




hangman = """-----
|   |
|
|
|
|
|
|
|
--------""",

"""-----
|   |
|  ( )
|
|
|
|
|
|
--------"""
"""
-----
|   |
|  ( )
| / | \
|   |
|   |
|
|
|
--------
"""

"""

|   |
|  ( )
| / | 
|   |
|   |
|
|
|
--------
"""
"""-----
|   |
|  ( )
| / | \
|   |
|   |
|
|
|
--------
"""
"""-----
|   |
|  ( )
| / | \ 
|   |  
|   |
|  /
| /
|
--------
"""
"""-----
|   |
|  ( )
| / | \ 
|   |  
|   |
|  / \
| /   \
|
--------"""
import numpy


# Print Hangman's current state
def printHangman(numberWrong):
    print hangman[0]
    # Print the hangman
    # print top of noose
    if numberWrong >= 1:
        print hangman[1]# print head
    else:
        print hangman[0] # don't print head
    if numberWrong >= 2:
        print hangman[2]# print neck
    else:
        print hangman[1]# don't print neck
    if numberWrong >= 3:
        print hangman[3]#  print arms # Backslash is a spacial character so using two creates one
    else:
        print hangman[2]# don't print arms
    if numberWrong >= 4:
        print hangman[4]# print body
    else:
        print hangman[3]# don't print body
    if numberWrong == 5:  # can't be > here so we get to the else :)
        print hangman[5]# print left leg
    elif numberWrong >= 6:
     print hangman[6]# print both legs
    else:
        print hangman[4]


# don't print any legs
# print bottom of noose

def printBlanks(word, correctLetters):
    # Set solved equal to true (innocent until proven guilty)
    # Loop over each letter in the word  for l in word:
    l = l.lower()  # not required but nice to have
    # Check if that letter is in the list of correct letters
    if False:  # Remove "False" and replace it with the appropriate condition
    # If it is, print the letter and a space
    else:


# If it isn't, print an underscore and a space
# Also, set solved equal to False
print();
print();
return solved

# Define a list of words as options


# Define a list to hold the correctly guessed letters

# Define a variable to count the number of incorrect guesses


# Pick a random word to be used

# Repeat forever, we'll use a break to get out

# Print the Status of the Hangman

# Print the word blanks and see if they solved it
solved = False  # Replace False with a function call

# Catch Death (Exit loop if they got 6 or more wrong)

if solved:
    print('You win!')
    break;  # no need to guess again

# Define a variable to hold user input
# Loop until they give a letter

# Check if the letter is in the word
if True:  # Replace True with the correct condition
# If it's right, put it in the correct letters list and let them know it was right
else:
# If it's wrong, increment the wrong count and let them know it was wrong
print();






# Reveal what the word was
hangman_status =  """-----
|   |
|
|
|
|
|
|
|
--------""",

"""-----
|   |
|  ( )
|
|
|
|
|
|
--------
"""
"""-----
|   |
|  ( )
|   |
|   |
|   |
|
|
|
--------
"""
"""
"""
"""-----
|   |
|  ( )
| / | \
|   |
|   |
|
|
|
--------
"""
"""-----
|   |
|  ( )
| / | \ 
|   |  
|   |
|  /
| /
|
--------
"""
"""-----
|   |
|  ( )
| / | \
|   |
|   |
|
|
|
-------------
|   |
|  ( )
| / | \
|   |
|   |
|
|
|
--------"""

