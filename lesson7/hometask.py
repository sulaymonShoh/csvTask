import json
import os.path
from multiprocessing import Process

files = os.listdir("./descriptions")


def printer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Sum of number in this file is {result}"

    return inner


@printer
def sum_of_numbers():
    global files
    for f in files:
        with open(f, 'r') as file:
            data = file.read().strip().split()
            data = list(filter(lambda x: x.isdigit(), data))
            return f"Sum of numbers in file {f} is {eval('+'.join(data))}"


def upper_words():
    global files
    for f in files:
        try:
            with open(f, 'r') as file:
                data = file.read().strip().split()
                data = list(filter(lambda x: x.istitle(), data))
        except FileNotFoundError:
            return "Exception: Such file does not exist!"
        else:
            with open('upper.txt', 'w') as file:
                file.write(' '.join(data))
            return "Result has been written successfully!"


def count_chars():
    global files
    result = []
    os.chdir("descriptions")
    for f in files:
        filedata = {
            "filename": f,
            "chars": {
                "numbers": {},
                "letters": {},
                "others": {}
            }
        }
        with open(f) as file:
            data = file.read()
            dataset = set(data)
            for i in dataset:
                if i in [' ', '\n']:
                    continue
                elif i.isdigit():
                    filedata["chars"]["numbers"].setdefault(i, data.count(i))
                elif i.isalpha():
                    filedata["chars"]["letters"].setdefault(i, data.count(i))
                else:
                    filedata["chars"]["others"].setdefault(i, data.count(i))
        result.append(filedata)
    os.chdir("..")

    with open("chars.json", "a") as jf:
        json.dump(result, jf, indent=4)
    print("chars.json has been written successfully")


if __name__ == '__main__':
    p1 = Process(target=sum_of_numbers)
    p2 = Process(target=upper_words)
    p3 = Process(target=count_chars)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
