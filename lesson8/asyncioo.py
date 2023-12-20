import requests
import asyncio


async def print_numbers():
    for i in range(10):
        print(i)


async def get_data():
    await asyncio.sleep(0.2)
    return {"data": 24}


async def run():
    await print_numbers()
    data = await get_data()
    print(data)

if __name__ == '__main__':
    asyncio.run(run())