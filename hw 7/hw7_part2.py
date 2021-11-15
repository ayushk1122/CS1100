# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:08:51 2021
This program uses two json files of movies and ratings and inputs the contents into a dictionary
It then asks for different user conditions and loops through until the user inputs 'stop' to
terminate the program
Runs through and finds the best and worst rated movie between the given years 
@author: Ayush
"""
import json

min_year = input("Min year => ")
print(min_year)
min_year = int(min_year)
max_year = input("Max year => ")
print(max_year)
max_year = int(max_year)
w1 = input("Weight for IMDB => ")
print(w1)
w1 = float(w1)
w2 = input("Weight for Twitter => ")
print(w2)
w2 = float(w2)
print()

"""
This function takes a list of twitter ratings for a specific movie as input and returns 
a float average 
"""
def average_twitter_rating (ratings):
    average = 0.0
    for rating in ratings:
        average += rating
    
    average = average / (len(ratings))
    return average 

"""
This function takes two float weight values, a specific movie rating, and a specific movie
qnd returns a combined rating float value calculated using the formula given in the spec
"""
def compute_rating (w1, w2, rating, movie):
    imdb_rating = movie['rating']
    avg_rating = average_twitter_rating(rating)
    comb_rating = (w1 * imdb_rating + w2 * avg_rating) / (w1 + w2)
    return comb_rating
    
    
## main program
if __name__ == "__main__":
    ## loads contents of json files into dictionaries 
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    ## list to hold (rating, movie) tuples so list can be sorted accordingly
    movie_ratings = []
    
    for key in movies:
        ## checks to make sure the movie year is within the correct bounds
        if (movies[key]['movie_year'] <= max_year and movies[key]['movie_year'] >= min_year):
            ## checks to make sure movie is in the twitter ratings
            if (key in ratings.keys()):
                ## makes sure twitter ratings list is greater then or equal to 3
                if (len(ratings[key]) >= 3):
                    ## uses compute rating to calculate rating for movie
                    mov_rating = compute_rating(w1, w2, ratings[key], movies[key])
                    movie_ratings.append((mov_rating, key))
    
    ## reverse sorts list to make sure highest ratings come first
    movie_ratings.sort(reverse = True)
                    
    genre = input ("What genre do you want to see? ")
    print(genre)
    print()
    ## lowers and titles input to avoid case sensitivity and match format of list of genres
    genre = genre.lower()
    genre = genre.title()

    while (genre.lower() != 'stop'):
        best = ()
        worst = ()
        
        ## finds best rated movie
        ## essentially finds the first occurence in list of tuples that has the inputted
        ## genre, since list is reverse sorted, first occurance would be the max
        for rate in movie_ratings:
            if (genre in movies[rate[1]]['genre']):
                ## tuple in form (rating score, movie id key)
                best = (rate[0], movies[rate[1]])
                ## breaks to avoid unnecessary looping
                break
        ## loops from last index in list of tuples to find worst rated movie
        ## finds the first occurance starting from the end of the list of tuples
        ## since this would be the minimum rating value movies
        i = (len(movie_ratings) - 1)
        while (i >= 0):
            if (genre in movies[movie_ratings[i][1]]['genre']):
                ## tuple in form (rating score, movie id key)
                worst = (movie_ratings[i][0], movies[movie_ratings[i][1]])
                break
            i -= 1
        
        ## checks for genre that does not exist within all movies
        if (len(best) == 0 and len(worst) == 0):
            print('No {} movie found in {} through {}\n'.format(genre.title(), min_year, max_year))
        else:
            print('Best:')
            print('        Released in {}, {} has a rating of {:.2f}\n'.format(best[1]['movie_year'], best[1]['name'], best[0]))
            print('Worst:')
            print('        Released in {}, {} has a rating of {:.2f}\n'.format(worst[1]['movie_year'], worst[1]['name'], worst[0]))
        
        ## asks for genre again to continue loop
        genre = input ("What genre do you want to see? ")
        print(genre)
        if (genre.lower() != 'stop'):
            print() 
        genre = genre.lower()
        genre = genre.title()
            