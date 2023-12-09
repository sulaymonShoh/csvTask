import requests
import os


class ContextManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(self.path, self.mode)
        self.file = file
        return file

    def __exit__(self):
        self.file.close()


if __name__ == '__main__':

    url = 'https://randomuser.me/api/'
    response = requests.get(url=url).json()
    response = response['results'][0]['picture']

    os.chdir('images')

    for i in response:
        with open(f'{i}.jpg', 'wb') as image:
            imagedata = requests.get(url=response[i]).content 
            image.write(imagedata)
