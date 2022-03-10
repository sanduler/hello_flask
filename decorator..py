import time


# this function is a decorator that adds sleep functionality to functions
# 1. this function takes a function as an argument
def delay_decorator(function):
    # the wrapper function us triggered at the return
    def wrapper():
        # 3.the program sleeps
        time.sleep(1)
        # 4. the program runs the desired function after 1 second of sleep
        function()
        function()

    # 2.the program function calls inside the wrapper function
    # 5. the program returns the delay_decorator back wit the value of the nested function
    return wrapper()


@delay_decorator
def say_hello():
    print("Hello")


def main():
    hello = say_hello()
    print(hello)


if __name__ == '__main__':
    main()
