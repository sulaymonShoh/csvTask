# decorators
import json


class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} hisobingiz: {self.balance}"


def logger(file, d: dict):
    data = load_data(file)
    data.append(d)
    save_data(file, data)


def load_data(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        open(file, 'x')
        data = []
    return data


def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


def checker(func):
    def inner(*args, **kwargs):
        p1, p2, amount = args
        report = {
                "sender": p1.name,
                "receiver": p2.name,
                "amount": amount,
                "successful": True
            }

        if p1.balance < amount:
            report["successful"] = False
            logger('log.json', report)

            print("Hisobingizda yetarli mablag' mavjud emas")

            return None

        result = func(*args, **kwargs)

        logger('log.json', report)
        print(f"{p1.name}dan {p2.name}ga transfer amalga oshirildi")

        return result

    return inner


@checker
def transfer(p1, p2, amount):
    p1.balance -= amount
    p2.balance += amount


if __name__ == '__main__':
    ali = Person("Ali", 2500)
    vali = Person("Vali", 1000)
    soli = Person("Soli", 500)

    print(ali)
    print(vali)
    print(soli)

    value = float(input("Transfer summasi: "))
    transfer(ali, vali, value)

    value = float(input("Transfer summasi: "))
    transfer(vali, soli, value)

    print(ali)
    print(vali)
    print(soli)
