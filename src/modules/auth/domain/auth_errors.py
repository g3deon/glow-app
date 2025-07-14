

class AuthExceptionError(Exception):
    pass

class AuthCredentialsError(Exception):
    def __init__(self, msg = 'Error with the credentials'):
        self.msg = msg
        super().__init__(msg)

