class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def __iter__(self):
        self.file = open(file=self.file_path)
        return self
    def __next__(self):
        line  = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()


if __name__ == '__main__':

    for line in FileReader("descriptions/001.txt"):
        print(line)