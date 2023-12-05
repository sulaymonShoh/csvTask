class FloatRange:
    def __init__(self, first, last=1, step=1):
        if last != 1:
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
        return val


if __name__ == '__main__':
    # FloatRange(12)
    # FloatRange(12,34)
    # FloatRange(12,34,0.5)

    for i in FloatRange(12, 20, 0.5):
        print(i)

    # a = ["ali", "vali", "zokir", "shokir"]

    # for name in a.__iter__():
    #     #iteratsiya iteration
    #     print(name)
    # it = a.__iter__()
    # print(it.__next__())
    # print(it.__next__())
    # print(it.__next__())
    # print(it.__next__())
    # # print(it.__next__())
    # iter = iter(a)
    # while True:
    #     try:
    #         val = next(iter)
    #         print(val)
    #     except StopIteration:
    #         break
