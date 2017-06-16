import random


def main():
    welcome = ['Welcome to Hangman!!']

    for line in welcome:



        play_again = True

        while play_again:

            words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                     "computer", "python", "program", "glasses", "sweatshirt",
                     "sweatpants", "mattress", "friends", "clocks", "biology",
                     "algebra", "suitcase", "knife", "ninjas", "shampoo"
                     ]

            chosen_word = random.choice(words).lower()
            player_guess = None
            guessed_letters = []
            word_guessed = []
            for letter in chosen_word:
                word_guessed.append("-")
            joined_word = None

            HANGMAN = (
                """
                -----
                |   |
                |
                |
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                |
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                |  -+-
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  | 
                |  | 
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  | | 
                |  | 
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  | | 
                |  | | 
                |
                --------
                """)

            print(HANGMAN[0])
            attempts = len(HANGMAN) - 1

