import numpy as np


########################################################
# These functions will be used in Phase 3 (skip for now)
########################################################

def findSimilar(iLike, userLikes):
    # Calculate the similarity
    userSimilarity = []
    for user in range(0, len(userLikes)):
        similarityAnd = len([i for i, item in enumerate(userLikes[user]) if item == 1 and iLike[i] == 1])
        userSimilarityOr = len([i for i, item in enumerate(userLikes[user]) if iLike[i] == 1 or item == 1])
        userSimilarity.append(similarityAnd / float(userSimilarityOr))
        # replace 0 with the correct code to calculate the Jaccard Index for each user

    # Make sure the most similar user has a new like that the previous user did not have
    # I used a while loop.
    # You can "get rid" of a user that is most similar, but doesn't have any new likes
    # by setting the userSimilarity for them to 0
    # When you get the index, save it in the variable maxIndex


    while True:
        maxIndex = userSimilarity.index(max(userSimilarity))
        if np.all(np.argwhere(userLikes[maxIndex] == 1) == np.argwhere(iLike == 1)):
            # if userLikes[maxIndex] == iLike:
            userSimilarity[maxIndex] = 0
        elif set(np.argwhere(userLikes[maxIndex] == 1).flatten()) < set(np.argwhere(iLike == 1).flatten()):
            userSimilarity[maxIndex] = 0
        else:
            break

    # Print the max similarity number (most times this is something like 0.17)
    print 'User Similarity: %s' % (max(userSimilarity))

    # Return the index of the user which is the best match
    return maxIndex


def printMovie(id):
    # Print the id of the movie and the name.  This should look something like
    # "    - 430: Duck Soup (1933)" if the id is 430 and the name is Duck Soup (1933)
    print '- ID %s: %s' % (id, movieNames[id - 1][1])  # replace 0 with the correct code


def processLikes(iLike):
    print("\n\nSince you like:")

    # Print the name of each movie the user reported liking
    # Hint: Use a for loop and the printMovie function.

    for i in iLike:
        printMovie(i)

    # Convert iLike into an array of 0's and 1's which matches the array for other users
    # It should have one column for each movie (just like the userLikes array)
    # Start with all zeros, then fill in a 1 for each movie the user likes
    iLikeNp = np.zeros((1, maxMovie + 1))  # replace 0 with the code to make the array of zeros
    iLikeNp = iLikeNp.flatten()
    # You'll need a few more lines of code to fill in the 1's as needed

    # iLike[:] = [x for x in iLike]
    iLikeNp[iLike] = 1

    # Find the most similar user
    user = findSimilar(iLikeNp, userLikes)  # replace 0 with the correct code (hint: use one of your functions)
    print("\nYou might like: ")

    # Find the indexes of the values that are ones
    # https://stackoverflow.com/a/17568803/3854385 (Note: You don't want it to be a list, but you do want to flatten it.)
    recLikes = np.argwhere(userLikes[user] == 1)  # replace 0 with the needed code
    recLikes = recLikes.flatten()

    # For each item the similar user likes that the person didn't already say they liked
    # print the movie name using printMovie (you'll also need a for loop and an if statement)
    for i in recLikes:
        if i not in iLike:
            printMovie(i)
        else:
            continue


########################################################
# Begin Phase 1
########################################################

# Load Data
# Load the movie names data (u.item) with just columns 0 and 1 (id and name) id is np.int, name is S128
movieNames = np.loadtxt('/Users/maanavkhaitan/Downloads/baseCode/ml-100k/u.item',
                        dtype={'names': ('id', 'name'), 'formats': (np.int, 'S128')}, delimiter='|',
                        usecols=(0, 1))  # replace 0 with the correct code to load the movie names

# Create a dictionary with the ids as keys and the names as the values
# movieDict = dict(enumerate(movieNames[:,1])) # replace 0 with the code to make the dict
movieDict = {}
for i in range(1, 1683):
    movieDict[i] = movieNames[i - 1][1]

# Load the movie Data (u.data) with just columns 0, 1, and 2 (user, movie, rating) all are np.int
movieData = np.loadtxt('/Users/maanavkhaitan/Downloads/baseCode/ml-100k/u.data',
                       dtype={'names': ('user', 'movie', 'rating'), 'formats': (np.int, np.int, np.int)},
                       usecols=(0, 1, 2))  # replace 0 with the correct cod eto load the movie data

# print(movieData)
# print(movieNames)

# exit(0) # Delete this after we finish phase 1, for now just get the data loaded

########################################################
# Begin Phase 2
########################################################

# Compute average rating per movie
# This is non-ideal, pandas, scipy, or graphlib should be used here

# Create a dictionary to hold our temporary ratings
movieRatingTemp = {}  # replace 0 with code for an empty dictionary

# For every row in the movie data, add the rating to a list in the dictionary entry
# for that movies ID (don't forget to initialize the dictionary entry)
entry = {}
for i in range(0, movieData.shape[0]):
    entry[movieData[i][1]] = []
for i in range(0, movieData.shape[0]):
    entry[movieData[i][1]].append(movieData[i][2])

# Create an empty dictionary for movieRating and movieRatingCount
movieRating = {}  # replace 0 with code for an empty dictionary
movieRatingCount = {}  # replace 0 with code for an empty dictionary

# Using numpy place the average rating for each movie in movieRating and the total number of ratings in movieRatingCount
# Note: You will need a for loop to get each dictionary key

for key in entry.keys():
    movieRating[key] = np.mean(entry[key])
    movieRatingCount[key] = len(entry[key])

# Get sorting ratings
# https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
movieRatingS = sorted(movieRating.iteritems(), key=lambda (k, v): (v, k), reverse=True)
"""
# Top 10 Movies
print("Top Ten Movies:")
# Print the top 10 movies
# It should print the number, title, id, rating and count of reviews for each movie
# ie 2. Someone Else's America (1995) (ID: 1599) Rating: 5.0 Count: 1
for i in range(1, 11):
    print '%s. %s (ID: %s) Rating: %s Count: %s' % (str(i), movieNames[(movieRatingS[i-1][0])-1][1], movieRatingS[i-1][0], movieRatingS[i-1][1], movieRatingCount[movieRatingS[i-1][0]])
# Top 10 Movies with at least 100 ratings    
print("\n\nTop Ten movies with at least 100 ratings:")
# It should print the same thing, but this time all the movies should have over 100 ratings
# The number should be the movie's absolute rank
# ie (16. Close Shave, A (1995) (ID: 408) Rating: 4.49 Count: 112)
# Number 16 is first in this list because it's the first movie with over 100 ratings
hundred_movies = [movieRating.items()[i-1] for i in range(1,1683) if movieRatingCount[i]>=100]
hundred_movieRatingS = sorted(hundred_movies, key=lambda (k,v): (v,k), reverse=True)
for i in range(1,11):
    print '%s. %s (ID: %s) Rating: %s Count: %s' % (movieRatingS.index(hundred_movieRatingS[i-1])+1, movieNames[(hundred_movieRatingS[i-1][0])-1][1], hundred_movieRatingS[i-1][0], hundred_movieRatingS[i-1][1], movieRatingCount[hundred_movieRatingS[i-1][0]])
"""

# exit(0) # Remove this line after we finish phase 2

########################################################
# Begin Phase 3
########################################################

# Create a user likes numpy ndarray so we can use Jaccard Similarity
# A user "likes" a movie if they rated it a 4 or 5
# Create a numpy ndarray of zeros with demensions of max user id + 1 and max movie + 1 (because we'll use them as 1 indexed not zero indexed)

# Find the max movie ID + 1
maxMovie = movieNames.shape[0] + 1  # replace 0 with the correct code

# Find the max user Id + 1
maxUser = movieData['user'].max() + 1  # replace 0 with the correct code

# Create an array of 0s which will fill in with 1s when a user likes a movie
userLikes = np.zeros((maxUser, maxMovie))

# Go through all the rows of the movie data.
# If the user rated a movie as 4 or 5 set userLikes to 1 for that user and movie
# Note: You'll need a for loop and an if statement

for i in range(0, movieData.shape[0]):
    if movieData[i][2] >= 4:
        userLikes[movieData[i][0], movieData[i][1]] = 1

########################################################
# At this point, go back up to the top and fill in the
# functions up there
########################################################
"""
# First sample user
# User Similiarity: 0.133333333333
iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)
# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603]
processLikes(iLike)
# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79,  96,  98, 168, 173, 176,194, 318, 357, 427, 603, 1]
processLikes(iLike)
"""
# If your code completes the above recommendations properly, you're ready for the last part,
# allow the user to select any number of movies that they like and then give them recommendations.
# Note: I recommend having them select movies by ID since the titles are really long.
# You can just assume they have a list of movies somewhere so they already know what numbers to type in.
# If you'd like to give them options though, that would be a cool bonus project if you finish early.


user_movie_ids = []


def take_user_input(input_title, print_out):
    out = [i for i, v in enumerate(movieNames) if input_title.lower() in v[1].lower()]
    if print_out == True:
        print 'Movies that match your search:'
        for item in out:
            printMovie(item + 1)
    if len(out) > 0:
        return True


def ask_user():
    while True:
        user_movie_id = raw_input('Search for a movie you like, or enter a movie ID, or type "done" if finished: ')
        # if int(user_movie_id) not in user_movie_ids:
        if user_movie_id == 'done':
            processLikes(user_movie_ids)
            break
        elif user_movie_id.isdigit() and int(user_movie_id) in user_movie_ids:
            print 'You have already liked this movie. Please enter another movie.'
        elif user_movie_id.isdigit() and int(user_movie_id) in movieNames['id']:
            user_movie_ids.append(int(user_movie_id))
            print '\'%s\' added to liked movies.' % (movieNames[int(user_movie_id) - 1][1])
        elif take_user_input(user_movie_id, False) == True:
            take_user_input(user_movie_id, True)
            user_selection = raw_input('Which of these movies do you like? (Enter Movie ID or b to go back)')
            if user_selection.isdigit() and int(user_selection) not in user_movie_ids and int(user_selection) in \
                    movieNames['id']:
                user_movie_ids.append(int(user_selection))
                print '\'%s\' added to liked movies.' % (movieNames[int(user_selection) - 1][1])
            elif user_selection == 'b':
                continue
            elif int(user_selection) in user_movie_ids:
                print 'You have already liked this movie. Please enter another movie.'
            else:
                print 'No movie matched your search. Please enter another movie.'
        else:
            print 'No movie matched your search. Please enter another movie.'
            continue
            # else:
            # print 'You have already liked this movie. Please enter another movie.'


def recommend_to_user():
    print 'Welcome to the Movie Recommender!'
    ask_user()
    while True:
        user_again = raw_input('Would you like to add other movies you like? (y/n)')
        if user_again == 'y':
            ask_user()
        elif user_again == 'n':
            print 'Thank you for using our movie recommender today!'
            break


recommend_to_user()

