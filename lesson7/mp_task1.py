from multiprocessing import Process


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def fib(n):
    res = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fib_print(n):
    print(fib(n))


def fact_print(n):
    print(fact(n))


if __name__ == '__main__':
    a = int(input("Factorial uchun son: "))
    b = int(input("Fibonacci uchun son: "))

    p1 = Process(target=fact_print, args=(a,))
    p2 = Process(target=fib_print, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
