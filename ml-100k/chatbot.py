from __future__ import print_function
import numpy as np

def findSimilar(iLike, userLikes):
    def printMovie(id):# Print the id of the movie and the name.  This should look something like
        print("   - "+str(id) + ": "+movieDict[id])# "    - 430: Duck Soup (1933)" if the id is 430 and the name is Duck Soup (1933)
    # replace 0 with the correct code

    # Create an And similarity
    similarityAnd = iLike * userLikes  # replace 0 with the correct code
    # Create a per user sum (this is the numerator of the jaccard index)

    similarityAndSum = similarityAnd.sum(axis=1)  # replace 0 with the correct code    def findSimilar(iLike, userLikes):

    # Create an Or similarity
    SimilarityOr = iLike + userLikes #replace 0 with the correct code
    userSimilarity = similarityAndSum / (np.sum(SimilarityOr, 1) - similarityAndSum)

    while True:
        maxIndex = userSimilarity.argmax()
        newLikes = userLikes[maxIndex] - iLike
        newCount = len(newLikes[newLikes > 0])
        if newCount > 0:
            break
        else:
            userSimilarity[maxIndex] = 0
    # Calculate the similarity


    # When you get the index, save it in the variable maxIndex
    print("\n User Similarity: "+str(userSimilarity[maxIndex]))
    return maxIndex

    # Print the max similarity number (most times this is something like 0.17
      # replace 0 with the correct code to calculate the Jaccard Index for each user

    # Make the most similar user has a new like that the previous user did not have
    # I used a while loop.
    # You can "get r
    # Return the index of the user which is the best match



def processLikes(iLike):
    print("\n\nSince you like:")
    for like in iLike:
        printMovie(like)
    # Print the name of each movie the user reported liking
    # Hint: Use a for loop and the printMovie function.

    # Convert iLike into an array of 0's and 1's which matches the array for other users
    # It should have one column for each movie (just like the userLikes array)
    # Start with all zeros, then fill in a 1 for each movie the user likes
    iLikeNp = np.zeros(maxMovie) # replace 0 with the code to make the array of zeros
    # You'll need a few more lines of code to fill in the 1's as needed
    for i in iLike:
        iLikeNp[i] = 1

    # Find the most similar user
    user = findSimilar(iLikeNp, userLikes)  # replace 0 with the correct code (hint: use one of your functions)
    print("\nYou might like: ")
    # Find the indexes of the values that are ones
    # https://stackoverflow.com/a/17568803/3854385 (Note: You don't want it to be a list, but you do want to flatten it.)
    recLikes = np.argwhere(userLikes[user, :] == 1).flatten()  # replace 0 with the needed code

    for like in recLikes:
        if iLikeNp[like] == 0:
            printMovie(like)

    # For each item the similar user likes that the person didn't already say they liked
    # print the movie name using printMovie (you'll also need a for loop and an if statement)




# Phase 1




# Load Data
# Load the movie names data (u.item) with just columns 0 and 1 (id and name) id is np.int, name is S128
movieNames = np.loadtxt('C:/Users/matth/DukeTip/ml-100k/u.item',
                        delimiter='|', usecols=(0,1),
                        dtype={'names':( 'id', 'name'),
                               'formats': (np.int, 'S128')}
                        )


                                                          # replace 0 with the correct code to load the movie names

# Create a dictionary with the ids as keys and the names as the values
movieDict = dict(zip(movieNames['id'], movieNames['name']))  # replace 0 with the code to make the dict
# Load the movie Data (u.data) with just columns 0, 1, and 2 (user, movie, rating) all are np.int
movieData = np.loadtxt('./u.data',
                       delimiter="\t", usecols=(0,1,2),
                       dtype={'names': ('user', 'movie', 'rating'),
                              'formats': (np.int, np.int, np.int)}
                       )



# replace 0 with the correct cod eto load the movie data






#Phase 2





# Compute average rating per movie
# This is non-ideal, pandas, scipy, or graphlib should be used here

# Create a dictionary to hold our temporary ratings
movieRatingTemp = {}  # replace 0 with code for an empty dictionary

# For every row in the movie data, add the rating to a list in the dictionary entry
# for that movies ID (don't forget to initialize the dictionary entry)

# Create an empty dictionary for movieRating and movieRatingCount
movieRating = {}  # replace 0 with code for an empty dictionary
movieRatingCount = {}  # replace 0 with code for an empty dictionary

# Using numpy place the average rating for each movie in movieRating and the total number of ratings in movieRatingCount
# Note: You will need a for loop to get each dictionary key


# Get sorting ratings
for row in movieData:
    if row['movie'] not in movieRatingTemp:
        movieRatingTemp[row['movie']] = [row['rating']]
    else:
        movieRatingTemp[row['movie']].append(row['rating'])



movieTotalRatings = {}



for key in movieRatingTemp:
    movieRating[key] = np.mean(movieRatingTemp[key])
    movieRatingCount[key] = len(movieRatingTemp[key])

#

# https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
movieRatingS = sorted(movieRating.iteritems(), key=lambda (k, v): (v, k), reverse=True)


# Top 10 Movies
print("Top Ten Movies:")
for i in range(0,11):
    print("Movie ID: " + str(movieRatingS[i][0]) + " Rating: "+
        str(movieRatingS[i][1]))
    print(movieDict[movieRatingS[i][0]])
    print(" Count: " + str(movieRatingCount[movieRatingS[i][0]]))
    print(movieRatingS[0][0])

print("")



# Print the top 10 movies
# It should print the number, title, id, rating and count of reviews for each movie
# ie 2. Someone Else's America (1995) (ID: 1599) Rating: 5.0 Count: 1


# Top 10 Movies with at least 100 ratings
print("\n\nTop Ten movies with at least 100 ratings:")

moviesPrinted = 0
i = 0
while moviesPrinted < 10:
    key = movieRatingS[i][0]
    if movieRatingCount[key] >= 100:
        moviesPrinted += 1
        print(str(i+1)+" Movie: "+str(movieDict[key])+
        " Rating: "+str(movieRatingS[i][1]),
        " Count: "+str(movieRatingCount[key]))
    i += 1






# It should print the same thing, but this time all the movies should have over 100 ratings
# The number should be the movie's absolute rank
# ie (16. Close Shave, A (1995) (ID: 408) Rating: 4.49 Count: 112)
# Number 16 is first in this list because it's the first movie with over 100 ratings

 # Remove this line after we finish phase 2




#Phase 3


#similarityand and divided similarityor minus sum


maxMovie = movieData['movie'].max()+1

# replace 0 with the correct code

# Find the max user Id + 1
maxUser = np.max(movieData['user']) + 1 # replace 0 with the correct code

# Create an array of 0s which will fill in with 1s when a user likes a movie
userLikes = np.zeros((movieData['user'].max()+1, maxMovie))

# Go through all the rows of the movie data.
# If the user rated a movie as 4 or 5 set userLikes to 1 for that user and movie
# Note: You'll need a for loop and an if statement
for row in movieData:
    if row['rating'] == 4 or row['rating'] == 5:
        userLikes[row['user'], row['movie']] = 1


########################################################
# At this point, go back up to the top and fill in the
# functions up there
########################################################

# First sample user
# User Similiarity: 0.133333333333
iLike = [655, 315, 66, 96, 194, 172]
processLikes(iLike)

# What if it's an exact match? We should return the next closest match
# Second sample case
# User Similiarity: 0.172413793103
iLike = [79, 96, 98, 168, 173, 176, 194, 318, 357, 427, 603]
processLikes(iLike)

# What if we've seen all the movies they liked?
# Third sample case
# User Similiarity: 0.170731707317
iLike = [79, 96, 98, 168, 173, 176, 194, 318, 357, 427, 603, 1]
processLikes(iLike)

# If your code completes the above recommendations properly, you're ready for the last part,
# allow the user to select any number of movies that they like and then give them recommendations.
# Note: I recommend having them select movies by ID since the titles are really long.
# You can just assume they have a list of movies somewhere so they already know what numbers to type in.
# If you'd like to give them options though, that would be a cool bonus project if you finish early.

while True:
    recommend = raw_input('Would you like some recommendations based on your interests: (y/n)')
    recommend.lower()
    print(recommend)
    if len(recommend) == 0 or recommend[0] != 'y':
        break
        iLike = []
        while True:
            answer = raw_input('Please enter a movie ID or enter done to get our movie recommendations:')
            try:
                movieInt = int(movie)
            except ValueError:
                movieInt = 0

            if len(movie) == 0:
                break
            elif movieInt < 1 or movieInt > maxMovie:
                print("Invalid Selection")
                continue
            else:f
                iLike.append(movieInt)
            if answer == 'done':
                break
            else:
                if answer.isdigit() and answer not in iLike:
                        iLike.append(answer)
                else:
                    print('That ID does not exist')
                processLikes(iLike)


#########################################################################
#WORK IN PROGRESS
#########################################################################



#I'm not very good at coding :(