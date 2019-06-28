from flask_jwt_extended.exceptions import NoAuthorizationError, WrongTokenError


class ApiException(Exception):

    def __init__(self,message,code):
        self.message=message
        self.code=code



def exception_wrapper(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as exception:
            return {"message": exception.message}, exception.code
        except NoAuthorizationError:
            return {"message":"missing  authorization"}, 401
        except WrongTokenError:
            return {"message":"wrong token"}, 401
    return inner