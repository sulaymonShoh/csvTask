from time import sleep
from multiprocessing import Process

def square(nums):
    result = []
    for n in nums:
        result.append(n**2)
        sleep(5)

    print(result)


def cube(nums):
    result = []
    for n in nums:
        result.append(n ** 3)
        sleep(5)

    print(result)


if __name__ == '__main__':
    nums = [2, 3, 4, 6]
    sleep(10)
    p1 = Process(target=square, args=(nums,))
    p2 = Process(target=cube, args=(nums,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()