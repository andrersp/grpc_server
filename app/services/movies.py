# -*- coding: utf-8 -*-
from messages.movies_pb2 import MessageResponse, MoviesList, Movies
import messages.movies_pb2_grpc as movies_pb2_grpc
from ext.database import Session
from models.movies import MoviesDb


class MoviesServiceServicer(movies_pb2_grpc.MoviesServiceServicer):

    def UpdateMovies(self, request, context):

        movies = request.movies

        result = self.insert_movies(movies)

        result = {"success": result}

        return MessageResponse(**result)

    def GetMovies(self, request, context):

        session = Session()
        movies = session.query(MoviesDb).all()

        movies_list = list(map(lambda x: {
            "title": x.title,
            "adult": x.adult
        }, movies))

        # print(movies_list)

        return MoviesList(movies=movies_list)

    def GetMovie(self, request, context):
        movie_id = request.movie_id

        session = Session()
        movie = session.query(MoviesDb).get(movie_id)

        if movie:
            return Movies(adult=movie.adult, title=movie.title, language=movie.language, genres=movie.genres)

    def insert_movies(self, movies: list = []):

        try:
            lst = []
            s = Session()

            i = 0
            for movie in movies:

                data = {
                    "title": movie.title,
                    "language": movie.language,
                    "adult": movie.adult,
                    "genres": [{"id": x.id, "name": x.name} for x in movie.genres]
                }

                movie = MoviesDb(**data)
                lst.append(movie)

                if i == 1000:
                    s.bulk_save_objects(lst)
                    s.commit()
                    lst.clear()
                    i = 0

                i += 1

            s.bulk_save_objects(lst)
            s.commit()
            return True
        except:
            return False
