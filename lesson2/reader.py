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
        if self.current_index-1 < len(self.files):
            file_path = os.path.join(self.directory, self.files[self.current_index])

            current_file = open(file_path)
            data = current_file.readlines()
            current_file.close()

            self.current_index += 1

            # return file_path.split('.')[0], data
            return data
        else:
            raise StopIteration


if __name__ == '__main__':
    for data in FileIterator('descriptions'):
        # with open(f'{name}.csv', 'r+') as newfile:
        #     obj_writer = csv.writer(newfile)
        #     obj_writer.writerow(['Name', 'Weight', 'Description'])
        #
        #     # Assuming data is a list of lines
        #     for line in data:
        #         obj_writer.writerow(line.strip().split(','))
        #         print(line)
        print(data)