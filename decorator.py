def bye_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
        print("Bye")
    return wrapper

@bye_decorator
def say_hello():
    print("Hello world!")
    

say_hello()


def description_decorator(func):
    def wrapper(*args, **kwargs):
        print("Distance:")
        result = func(*args, **kwargs)
        if result < 100:
            print("Fast")
        else:
            print("Slow")
        return result
    return wrapper


@description_decorator
def distance(km, time):
    return km / time

print(distance(100, 10))