import os
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path # accepts directory, not file
        self.index=0
        self.files = [f for f in os.listdir(self.file_path)]
        self.cfile = self.file_path + self.files[self.index]
    def __iter__(self):

        self.file = open(self.cfile)
        return self
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.index += 1
            self.file.close()
        return line.strip()


if __name__ == '__main__':
    with open('output.csv', 'w') as res:
        for line in FileReader("descriptions/"):
            res.write(line)