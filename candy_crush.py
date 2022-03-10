import time

current_time = time.time()
print(current_time)


def decorator(function):
    def wrapper():
        print("Hello")
        print(function(3, 4))

    return wrapper


@decorator
def sum(number1, number2):
    return number1 + number2

@decorator
def diffrence(number1, number2):
    return number1 - number2


def main():
    sum()
    diffrence()


if __name__ == '__main__':
    main()
