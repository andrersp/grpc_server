# -*- Coding: utf-8 -*-

class CustomError(Exception):

    def __init__(self, code_err, message="Service Error"):
        self.code_err = code_err
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> code: {self.code_err}'


class FatalError(Exception):

    def __init__(self, code_err, message="Service Fatal Error"):
        self.code_err = code_err
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> code: {self.code_err}'
