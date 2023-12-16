import os.path


def printer(func):
    def inner(*args, **kwargs):
        if os.path.exists(args[0]):
            result = func(*args, **kwargs)
            return f"Sum of number in this file is {result}"
        return "Exception: Such file does not exist!"
    return inner


@printer
def sum_of_numbers(file):
    with open(file, 'r') as file:
        data = file.read().strip().split()
        data = list(filter(lambda x: x.isdigit(), data))
        return eval('+'.join(data))


def upper_words(file):
    try:
        with open(file, 'r') as file:
            data = file.read().strip().split()
            data = list(filter(lambda x: x.istitle(), data))
    except FileNotFoundError:
        return "Exception: Such file does not exist!"
    else:
        with open('upper.txt', 'w') as file:
            file.write(' '.join(data))
        return "Result has been written successfully!"


print(upper_words("./descriptions/1.txt"))
