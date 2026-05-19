"""
Decorator adds functionality without modifying original function.
"""
def logger(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@logger
def hello():
    print("Hello")

hello()