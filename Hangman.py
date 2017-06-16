import numpy

welcome = ['Welcome to Hangman! A word will be chosen at random and',
'you must try to guess the word correctly letter by letter',
'before you run out of attempts. Good luck!'
               ]
print welcome

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
"""-----
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




letter = raw_input("Please enter a letter:")
print letter

print hangman_status[0]

numberWrong = []

def printHangman(numberWrong):
    print hangman_status[numberWrong]

blanks = "_ "

def printBlanks(word, correctLetters):
    solved = True # Set solved equal to true (innocent until proven guilty)
    # Loop over each letter in the word
    for l in word:
        l = l.lower()  # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctLetters:  # Remove "False" and replace it with the appropriate condition
            print l+ ' ', # If it is, print the letter and a space
        else:
            print '_ ',# If it isn't, print an underscore and a space

            solved = False# Also, set solved equal to False
    print()
    print()
    return solved

my_list = ["duketip", "intelligence", "umbrella", "pizza", "matthew", "chicken", "knife"]
# Define a list of words as options


correctLetters = []# Define a list to hold the correctly guessed letters
word = numpy.random.choice(my_list)
incorrect = len(numberWrong)
print incorrect# Define a variable to count the number of incorrect guesses

# Pick a random word to be used

while True:# Repeat forever, we'll use a break to get out
    print hangman_status(incorrect) # Print the Status of the Hangman
    print blanks # Print the word blanks and see if they solved it
    solved = print blanks(word, correctLetters)
    break# Replace False with a function call

# Catch Death (Exit loop if they got 6 or more wrong)

if solved:
        print('You win!')
     # no need to guess again

user_input = 0# Define a variable to hold user input
# Loop until they give a letter

# Check if the letter is in the word
if correctLetters >= 5:
    print("You Win!")# Replace True with the correct condition
print correctLetters# If it's right, put it in the correct letters list and let them know it was right

print numberWrong# If it's wrong, increment the wrong count and let them know it was wrong
if correctLetters = len(word:):

print word

# Reveal what the word was











letter = raw_input("Please enter a letter:")
print letter
print raw_input
