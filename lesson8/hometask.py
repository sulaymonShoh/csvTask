import aiohttp
import json
import asyncio

url = "https://api.agify.io?name="


def read_json():
    with open("result.json", 'r') as file:
        return json.load(file)


def write_json(data):
    with open("result.json", 'w') as file:
        json.dump(data, file, indent=4)


async def get_data(name):
    async with aiohttp.ClientSession() as client:
        response = await client.get(url=url + name)
        print(f"working with {name}")

        json_data = read_json()
        json_data.append(await response.json())
        write_json(json_data)


async def run(arr):
    tasks = [get_data(i) for i in arr]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    names = input().split()
    asyncio.run(run(names))
