
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        # print the name
        # print the name of the dunction and the argument of the function that were passed
        print(f"You called {function.__name__}{args}")
        # calculate the result by passing the arguments to the actual a function
        result = function(args[0], args[1], args[2])
        # print the result
        print(f"It returned {result}")

    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
