import os


def printer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Sum of number is this file is {result}"
    return inner


def sum_of_numbers(directory):
    files = os.listdir(directory)
    os.chdir(directory)

    for f in files:
        with open(f) as file:
            data = file.read().strip().split()
            data = [int(x) for x in data if x.isdigit()]
            print(sum(data))
            # return sum(data)


print(sum_of_numbers("descriptions"))
