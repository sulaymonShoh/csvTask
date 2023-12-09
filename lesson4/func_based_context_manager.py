import datetime
import json
import os
from contextlib import contextmanager


@contextmanager
def file_manager(file, mode='r'):
    file = open(file, mode)

    try:
        with open('log.txt', 'w+') as log:
            log.write(f"file {datetime.datetime.now()} da {mode} rejimida ochildi")
        yield file
    finally:
        with open(f'{file}_log', 'a') as log:
            log.write(f"file {datetime.datetime.now()} da yopildi\n")
        file.close()


if __name__ == '__main__':
    os.chdir("json_files")
    with file_manager('jokes.json') as file:
        data = json.load(file)

    room1, room2, room3 = [], [], []
    for i in data:
        if i["id"] < 10: room1.append(i)
        elif i['id'] < 100: room2.append(i)
        else: room3.append(i)

    with file_manager('room1.json', 'w') as f1, file_manager('room2.json', 'w') as f2, file_manager('room3.json', 'w') as f3:
        json.dump(room1, f1, indent=4)
        json.dump(room2, f2, indent=4)
        json.dump(room3, f3, indent=4)

