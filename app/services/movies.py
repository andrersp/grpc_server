# -*- coding: utf-8 -*-
import grpc
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

        page = request.page or 1
        limit = request.limit or 20

        session = Session()
        query = session.query(MoviesDb)
        total = query.count()
        total_page = int(total / limit)

        if page > 1:
            query = query.offset((page - 1) * limit)
        query = query.limit(limit)

        movies = query.all()

        movies_list = list(map(lambda x: {
            "id": x.id,
            "title": x.title,
            "adult": x.adult,
            "language": x.language
        }, movies))

        result = {"movies": movies_list,
                  "actual_page": page,
                  "total_pages": total_page,
                  "itens": query.count(),
                  "total_itens": total,
                  "success": True}

        return MoviesList(**result)

    def GetMovie(self, request, context):
        movie_id = request.movie_id

        session = Session()
        movie = session.query(MoviesDb).get(movie_id)

        if not movie:
            msg = "Movie not found!"
            context.set_details(msg)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return Movies(success=False)

        if movie:
            return Movies(id=movie.id, adult=movie.adult, title=movie.title, language=movie.language, genres=movie.genres, success=True)

    def insert_movies(self, movies: list = []):
        session = Session()
        session.execute('TRUNCATE TABLE movies RESTART IDENTITY;')
        session.commit()
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
