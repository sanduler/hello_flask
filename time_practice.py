import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    """This a wrapper function that takes the function as an input and
    then raps the passed function with the wrapper."""
    def wrapper_function():
        # set the start time to a variable
        start_time = time.time()
        # function call the function that is passed
        function()
        # get the endtime
        end_time = time.time()
        # calculate the diffrence for the run speed for the fast function/slow function
        print(f"{function.__name__} run speed: {abs(start_time - end_time)}")

    return wrapper_function


@speed_calc_decorator
def fast_functions():
    # user a for loop to go through a million interactions
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    # user a for loop to go through a million interactions
    for i in range(100000000):
        i * i


def main():
    # function call both functions
    fast_functions()
    slow_function()


if __name__ == "__main__":
    main()
