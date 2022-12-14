#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
class ClassicMovie:
    '''
    Implement the __init__ function for a ClassicMovie class, which
    takes in a "movie_title", a "genre", a "director", and a
    "year_of_release". Each ClassicMovie object should also have a Boolean
    "has_watched" which is initially False, and a float "rating",
    which initially is 0.0.

    Create an instance method called "watched_it(my_rating)", 
    which, when called,
    sets self.has_watched to True, and sets self.rating to my_rating.
    
    Then implement the external function return_best_watched_classic().
    '''
    def __init__(self, movie_title, genre, director, year_of_release) :
        # GIVEN CODE
        self.movie_title = movie_title
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.has_watched = False
        self.rating = 0.0
        pass
    def watched_it(self, my_rating) :
        # YOUR CODE GOES HERE
        self.has_watched = True
        self.rating = my_rating
        pass
def return_best_watched_classic(classic_movie_list):
    '''
    In this method, iterate over all movies in the list of
    ClassicMovies "classic_movie_list". Find and return the
    ClassicMovie in the list that has the highest rating.

    For example, if you create 3 ClassicMovies via the syntax:
    c1 = ClassicMovie("The Thing", "horror", "john carpenter", 1982)
    c2 = ClassicMovie("Alien", "sci fi", "ridley scott", 1979)
    c3 = ClassicMovie("The Terminator", "action", "james cameron", 1984)
    Then call
    c1.watched_it(8.8)
    c2.watched_it(9.6)
    Then return_best_watched_classic([c1, c2, c3]) should return c2
    '''
    bestMovie = None
    for movie in classic_movie_list:
        if movie.rating != 0:
            if bestMovie == None:
                bestMovie = movie
            else:
                if movie.rating > bestMovie.rating:
                    bestMovie = movie
    return bestMovie
    # YOUR CODE GOES HERE
    pass
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        c1 = ClassicMovie("The Thing", "horror", "john carpenter", 1982)
        self.assertEqual(c1.movie_title, "The Thing")
    def test2(self):
        c2 = ClassicMovie("Alien", "sci fi", "ridley scott", 1979)
        self.assertEqual(c2.genre, "sci fi")
    def test3(self):
        c3 = ClassicMovie("The Terminator", "action", "james cameron", 1984)
        self.assertEqual(c3.director, "james cameron")
        self.assertEqual(c3.year_of_release, 1984)
    def test4(self):
        c1 = ClassicMovie("The Thing", "horror", "john carpenter", 1982)
        self.assertEqual(c1.has_watched, False)
        self.assertEqual(c1.rating, 0.0)
        c1.watched_it(8.8)
        self.assertEqual(c1.has_watched, True)
        self.assertEqual(c1.rating, 8.8)
    def test5(self):
        c1 = ClassicMovie("The Thing", "horror", "john carpenter", 1982)
        c2 = ClassicMovie("Alien", "sci fi", "ridley scott", 1979)
        c3 = ClassicMovie("The Terminator", "action", "james cameron", 1984)
        c2.watched_it(9.6)
        c3.watched_it(8.3)
        ans = return_best_watched_classic([c1, c2, c3])
        self.assertEqual(ans, c2)
    def test6(self):
        c1 = ClassicMovie("The Thing", "horror", "john carpenter", 1982)
        c2 = ClassicMovie("Alien", "sci fi", "ridley scott", 1979)
        c3 = ClassicMovie("The Terminator", "action", "james cameron", 1984)
        c1.watched_it(8.8)
        c2.watched_it(9.6)
        c3.watched_it(8.3)
        ans = return_best_watched_classic([c1, c3])
        self.assertEqual(ans, c1)
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
