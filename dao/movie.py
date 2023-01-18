from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_dic):
        new_movie = Movie(**movie_dic)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_dic):
        movie = self.get_one(movie_dic('id'))
        movie.title = movie_dic.get('title')
        movie.description = movie_dic.get('description')
        movie.trailer = movie_dic.get('trailer')
        movie.year = movie_dic.get('year')
        movie.rating = movie_dic.get('rating')
        movie.genre_id = movie_dic.get('genre_id')
        movie.director_id = movie_dic.get('director_id')

        self.session.add(movie)
        self.session.commit()


