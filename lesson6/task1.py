import json
from threading import Thread
from time import time

res = []


def counter(n):
    with open(f"data/file{n}.txt", "r") as file:
        data = file.read()
        numbers = list(filter(lambda x: x.isdigit(), data))
        summ = sum(list(map(int, numbers)))
        dic = {"filename": f"file{n}.txt", "yigindi": f"{summ}"}
        res.append(dic)

    with open('data/result.json', 'w') as file:
        json.dump(res, file, indent=4)


if __name__ == '__main__':
    threads = []
    t1 = time()
    for i in range(1, 5):
        t = Thread(target=counter, args=(i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()
    t2 = time()
    print(t2-t1)
