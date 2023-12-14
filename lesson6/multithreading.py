from threading import Thread
import requests


def get_user_data(id: int):
    print(f"{id} File opened")
    response = requests.get(url=f"https://jsonplaceholder.typicode.com/users/{id}")
    data = response.json()
    # print(data["name"], data["username"])

    with open(f"users/{id}.txt", "w") as f:
        f.write(f"name: {data["name"]}\nusername: {data["username"]}")
    print(f"{id} File closed")


if __name__ == '__main__':
    threads = []
    for i in range(1, 9):
        t = Thread(target=get_user_data, args=(i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()
