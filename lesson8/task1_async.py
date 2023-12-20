import asyncio


async def print_prime(n):
    # print()
    for i in range(2, n):
        qoldiqlar = []

        for j in range(2, i):
            qoldiqlar.append(i % j)

        if all(qoldiqlar):
            # await asyncio.sleep(0.2)
            print(i)


async def run(numbers):
    tasks = [asyncio.create_task(print_prime(number)) for number in numbers]
    asyncio.gather(*tasks)


if __name__ == '__main__':
    numbers = list(map(int, input("4 ta son kiriting: ").split()))
    asyncio.run(run(numbers))
