def fibonacci(n):
    i, a, b = 0, 0, 1
    while i <= n:
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            yield a+b
            a, b = b, a+b
        i += 1


for j in fibonacci(20):
    print(j)
