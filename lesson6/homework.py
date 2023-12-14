from threading import Thread
import requests
import os


"""
 - Berilgan urldan rasmlarni olish - done
 - ularni idsi bilan nomlangan faylga yozish - done
 - yuqoridagi tasklarni bajarishda multithreadingni qollash - done
"""


def write_image(f, data):
    with open(f'{f}.jpg', 'wb') as image:
        image.write(data)


def get_image(number):
    url = f"https://randomuser.me/api/portraits/thumb/men/{number}.jpg"

    response = requests.get(url=url)
    data = response.content

    write_image(number, data)


if __name__ == '__main__':
    os.mkdir("images")
    os.chdir("images")
    threads = []
    for i in range(1, 100):
        t = Thread(target=get_image, args=(i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

