from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper



