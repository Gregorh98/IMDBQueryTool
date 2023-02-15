from imdb import Cinemagoer
ia = Cinemagoer()


class Movie():
    movieId     = None
    movieTitle  = None
    genres      = []
    year        = None
    score       = None

    def __init__(self, title, score):
        movieDetails = ia.search_movie(title)[0]
        movie = ia.get_movie(movieDetails.movieID)

        self.score = score
        self.movieTitle = movieDetails
        self.movieId = movieDetails.movieID
        self.genres = ia.get_movie(self.movieId)["genres"]
        self.year = ia.get_movie(self.movieId)["year"]


m = Movie("Tron", 8.5)

print(m.movieId, m.movieTitle, m.genres, m.score, m.year)


