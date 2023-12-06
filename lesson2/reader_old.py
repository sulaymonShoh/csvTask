import os
import csv


class FileIterator:
    def __init__(self, directory):
        self.directory = directory
        self.files = [i for i in os.listdir(self.directory)]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index - 1 < len(self.files):
            file_path = os.path.join(self.directory, self.files[self.current_index])

            current_file = open(file_path)
            data = current_file.readlines()
            current_file.close()

            self.current_index += 1
            return file_path.split('.')[0], data
        else:
            raise StopIteration


if __name__ == '__main__':
    for name, data in FileIterator('descriptions'):
        # os.remove(f'{name}.csv')
        with open('output.csv', 'a') as newfile:
            for line in data:
                newfile.write(line)
