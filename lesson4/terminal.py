"""
    Homework
    08-12-2023

    Terminal dasturi

    * timerdan keyin terminalni tozalash buyrug'i Pycharm terminalida ishlamaydi. Powershell yoki Terminal da ishga tushirish tavsiya etiladi

"""

import os
from time import sleep

command_list = ['help', 'ls', 'touch', 'delete', 'mkdir', 'rmdir', 'cd', 'move', 'timer', '\\q']
status = True
timer = True


def ls():
    print(f"- {os.getcwd()} manzildagi fayllar va papkalar ro'yxati")
    print(" -", *os.listdir(os.getcwd()))
    if timer:
        sleep(10)
        os.system('cls')


def touch():
    try:
        filename = input("- Yangi fayl nomini kiriting: ")
        open(filename, 'x')
    except FileExistsError:
        print(" - Bunday fayl avvaldan yaratilgan. Bunday nom bilan yangi fayl yaratolmaysiz.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- \"{os.getcwd()+'\\'+filename}\" nomli fayl muvaffaqqiyatli hosil qilindi")
    if timer:
        sleep(7)
        os.system('cls')


def delete():
    try:
        filename = input("- O'chirish uchun fayl nomini kiriting:\n- ")
    except FileNotFoundError:
        print("- Bunday nomli fayl topilmadi. Qayta urining")
    except:
        print("Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- {filename} muvaffaqqiyatli o'chirildi")
    if timer:
        sleep(7)
        os.system('cls')


def mkdir():
    try:
        dname = input("- Yangi papka nomini kiriting: ")
        os.mkdir(dname)
    except FileExistsError:
        print("- Bunday papka avvaldan yaratilgan. Bunday nom bilan yangi papka yaratolmaysiz.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- {dname} nomli papka muvaffaqqiyatli yaratildi")
    if timer:
        sleep(7)
        os.system('cls')


def rmdir():
    try:
        dname = input("- O'chirish uchun papka nomini kiriting: ")
        os.mkdir(dname)
    except FileNotFoundError:
        print("- Bunday papka topilmadi")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"- {dname} nomli papka muvaffaqqiyatli o'chirildi")
    if timer:
        sleep(6)
        os.system('cls')


def cd():
    try:
        directory = input("- Yangi joylashunvi kiriting: ")
        os.chdir(directory)
    except FileNotFoundError:
        print("- Bunday manzil mavjud emas")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print(f"{os.getcwd()} - Joylashuv o'zgartirildi")
    if timer:
        sleep(6)
        os.system('cls')


def move():
    try:
        filename = input("- Ko'chirmoqchi bo'lgan faylingiz manzilini kiriting: ")
        dest = input("- Fayl uchun yangi manzilni kiriting: ")
        os.rename(filename, dest)
    except FileExistsError:
        print(
            "- Ko'chirish jarayonida xatolik yuz berdi. Sabablari quyidagilardan biri bo'lishi mumkin:\n  - Fayl yangi "
            "manzilida fayl nomini yozmadingiz\n  - Ko'chirmoqci bo'lgan faylingiz nomi bilan boshqa fayl bu manzilda "
            "avvaldan mavjud.")
    except FileNotFoundError:
        print("- Bunday fayl topilmadi.")
    except:
        print("- Xatolik yuz berdi. Qayta urining")
    else:
        print("- Muvaffaqqiyatli ko'chirildi")
    if timer:
        sleep(7)
        os.system('cls')


def help(arr):
    print(
        "- Dasturda mavjud buyruqlar ro'yxati:\n"
        "  - ls     ->  Hozirgi manzildagi fayllar va papkalar ro'yxati ko'ring\n"
        "  - cd     ->  Yangi manzilga o'tish\n"
        "  - touch  ->  Ko'rsatilgan nom bilan yangi fayl yaratish\n"
        "  - delete ->  Ko'rsatilgan faylni o'chirish\n"
        "  - mkdir  ->  Ko'rsatilgan nom bilan yangi papka yaratish\n"
        "  - rmdir  ->  Ko'rsatilgan nomli papkani o'chirish\n"
        "  - move   ->  Ko'rsatilgan faylni ko'rsatilgan manzilga ko'chirish\n"
        "  - timer  ->  Timerni o'chirish/yoqish"
    )

    input("- Davom etish uchun ENTER tugmasini bosing...")


def _timer():
    global timer
    timer = not timer


print("- Xush kelibsiz! Siz terminalning ba'zi funksiyalarini o'z ichiga olgan dsturni ishga tushirdingiz.")
print("- Har bir buyruqdan so'ng terminalni o'chirish uchun taymer o'rnatilgan. Uni timer buyrug'i orqali "
      "ochirish/yoqish mumkin")

while status:
    command = input("\n- Buyruqni kiriting: ")
    if command in command_list:
        if command == 'ls':
            ls()
        elif command == 'touch':
            touch()
        elif command == 'delete':
            delete()
        elif command == 'mkdir':
            mkdir()
        elif command == 'rmdir':
            rmdir()
        elif command == 'cd':
            cd()
        elif command == 'move':
            move()
        elif command == 'help':
            help(command_list)
        elif command == 'timer':
            _timer()
        elif command == '\\q':
            status = False
    else:
        print("- Buyruq noto'g'ri kitirildi. Qayta kiriting")
        print("  ESLATMA: help buyrug'i orqali buyruqlar ro'yxatini olishingiz mumkin")
        input("  Davom etish uchun ENTER tugmasini bosing...")
        continue

print("Dastur yakunlandi")
