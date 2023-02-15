from imdb import Cinemagoer
ia = Cinemagoer()

class Movie():
    movieId     = None
    movieTitle  = None
    genres      = []
    year        = None
    country     = None
    runtime     = None
    score       = None
    cast        = []

    def __init__(self, title, score):
        movieDetails = ia.search_movie(title)[0]
        movie = ia.get_movie(movieDetails.movieID)

        self.score = score
        self.movieTitle = movieDetails
        self.movieId = movieDetails.movieID
        self.genres = movie["genres"]
        self.year = movie["year"]
        self.runtime = movie["runtime"][0]
        self.country = movie["country"][0]
        for person in movie["cast"]:
            self.cast.append(person["name"])


m = Movie("Cast Away", 8.5)

print(m.movieId,
      m.movieTitle,
      m.genres,
      m.score,
      m.year,
      m.runtime,
      m.country,
      m.cast)


