# -*- coding: utf-8 -*-

import grpc
from concurrent import futures
import os

from movies_pb2 import MessageResponse

import movies_pb2_grpc

from app.models.movies import MoviesDb
# from app.ext.database import db

cwd = os.getcwd()

print("*" * 50)

print(cwd)
print("*" * 50)


class UpdateMoviesServicer(movies_pb2_grpc.UpdateMoviesServicer):

    def Update(self, request, context):

        movies = request.movies
        result = {"success": True}

        return MessageResponse(**result)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    movies_pb2_grpc.add_UpdateMoviesServicer_to_server(
        UpdateMoviesServicer(), server)

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
