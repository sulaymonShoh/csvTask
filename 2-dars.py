# task1 - done
# text = input()
# numbers = reversed(list(filter(lambda x: x.isdigit(), list(text))))
# print(*numbers)

# object
# mutable & immutable
# hashable & unhashable
# reference count
# heap & stack

# iteration
# obj.__iter__()

class FloatRange:
    # def __init__(self, *args):
    #     if len(args) == 1:
    #         self.first = 0
    #         self.last = args[0]
    #         self.step = 0.1
    #     elif len(args) == 2:
    #         self.first = args[0]
    #         self.last = args[1]
    #         self.step = 0.1
    #     else:
    #         self.first = args[0]
    #         self.last = args[1]
    #         self.step = args[2]
    def __init__(self, first, last=1, step=1):
        if last!=1:
            self.first = first
            self.last = last
        else:
            self.first = 1
            self.last = first
        self.step = step
    def __iter__(self):
        return self

    def __next__(self):
        val = self.first
        self.first += self.step
        if self.first > self.last:
            raise StopIteration
        else:
            return round(val, 2)


for i in FloatRange(1):
    print(i)
