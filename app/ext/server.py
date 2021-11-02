# -*- coding: utf-8 -*-

from signal import signal, SIGTERM
import grpc
from concurrent import futures
import os

from services.movies import MoviesServiceServicer
from messages.movies_pb2 import MessageResponse
import messages.movies_pb2_grpc as movies_pb2_grpc


def server():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    movies_pb2_grpc.add_MoviesServiceServicer_to_server(
        MoviesServiceServicer(), server)

    server.add_insecure_port("[::]:50051")
    server.start()

    def handle_sigterm(*_):
        print("Received Shutdown Signal")
        all_rpcs_done_event = server.stop(10)
        all_rpcs_done_event.wait(10)
        print("Shut down gracefully")

    server.wait_for_termination()
