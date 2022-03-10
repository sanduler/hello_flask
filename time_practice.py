import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {abs(start_time - end_time)}")

    return wrapper_function


@speed_calc_decorator
def fast_functions():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


def main():
    fast_functions()
    slow_function()


if __name__ == "__main__":
    main()
