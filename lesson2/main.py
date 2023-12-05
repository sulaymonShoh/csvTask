"""
"ez0zb5k 9 -sin8da 6q5ydi"

5 6 8 9 5 0



"""
from sys import getrefcount

# funksiya rekursiya bolishi uchun :
# - funksiya ichida oziga murojat
# - toxtash/bajarilishi sharti

"""
""
# def reverse_numbers(s:str) -> None:
#     if s[-1].isdigit():
#         print(s[-1],end=" ")
#     if len(s)!=1:
#         reverse_numbers(s[:-1])
# if __name__ == '__main__':
#     s = "ez0zb5k 9 -sin8da 6q5ydi"
#     reverse_numbers(s)
#     s = s[::-1]
#     print()
#     print(*list(filter(lambda x: x.isdigit(), s)))

object
mutable & immutable
hashable & unhashle
sequence
reference count
heap & stack
"""
if __name__ == '__main__':
    # data type int, float str bool None complex, list tuple set dict
    # int float bool None complex not iterable
    # list tuple set dict str
    z = 2345
    # a = ["ali", "vali", "zokir", "shokir"]
    # iteraion = iter(z)
    # print(next(iteraion))
    # print(next(iteraion))
    # print(next(iteraion))
    # print(next(iteraion))
    # print(next(iteraion))
    # print(type(z))
    # object -> variable name, value, id
    # print(id(z))
    # print(z)
    # squence = iterable +ordered -> list str, dict, tuple
    # hashable -> None int float str tuple
    # unshable -> set list
    a = ["ali", "vali", "zokir", "shokir"]
    # print(id(a))
    a.append("salim")
    # print(id(a))
    # a = "ali"
    # print(id(a))
    # a = a + " salim"
    # print(id(a))
    # print(hash(a))
    # print(hash(a))

    # getrefcount()
    # z = ("ali", "vali", "zokir", "shokir")
    # z2 = ("ali", "vali", "zokir", "shokir")
    # z3 = ("ali", "vali", "zokir", "shokir")
    # z4 = ("ali", "vali", "zokir", "shokir")
    # z5 = ("ali", "vali", "zokir", "shokir")
    # z2 = ["ali", "vali", "zokir", "shokir"]
    # z2 = ["ali", "vali", "zokir", "shokir"]
    # print(getrefcount(({"salom": 32, 3242: "3224we"})))
# https://realpython.com/python-memory-management/
""""
heap           stack
 z1  -        [32,23,324]
 z2  />         
 a1      ->   (32,23)
 a2      ->   (32,23)
            [-5; 256]
 
 
a       ->       45
z       ->       65
"""


