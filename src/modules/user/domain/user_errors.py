
class UserNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__('User Not Found')

class UserCreationError(Exception):
    def __init__(self, msg='Error creating user'):
        self.msg = msg
        super().__init__(msg)