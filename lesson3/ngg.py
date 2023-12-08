"""
Number guessing game
Played with computer
a UI will be designed
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint

SHARTLAR = """O'yin shartlari
1. Sizda son oralig'ini tanlash imkoni mavjud
2. Sizda vaqt cheklangan bo'ladi.
Qancha vaqt berilishini o'zingiz belgilaysiz

Tayyor bo'lsangiz quyidagi tugmani bosing
"""

TITLE = "Son topish o'yini"
USERTIME = 0
A=0
B=0

class Game:
    def __init__(self):
        self.A = A
        self.B = B
        self.countdownTime = USERTIME
        self.FOUND_STATUS = 1
        
        self.window = tk.Tk()
        self.window.title(TITLE)
        self.window.focus_set()
        self.window.geometry('640x360')
        self.window.configure(padx=20, pady=20)

        self.title = tk.Label(self.window, text=TITLE, font=('Arial', 18), pady=20)
        self.title.grid(row=0, column=0)

        self.mainEntry = tk.Entry(self.window, font=('Arial', 16), width=15)
        self.mainEntry.grid(row=1, column=0)

        self.confirmbtn = tk.Button(self.window, text='Tekshir', font=('Arial', 14), command=self.check)
        self.confirmbtn.grid(row=1, column=1)

        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.grid(row=2, column=0, columnspan=4, sticky='ew', padx=10, pady=20)

        self.countdownTitle = tk.Label(self.window, text='Qolgan vaqt', font=('Arial', 16), pady=20)
        self.countdownTitle.grid(row=3, column=0)
        
        self.countdownText = tk.Label(self.window, text=self.countdownTime, font=('Arial', 16), pady=10)
        self.countdownText.grid(row=4, column=0)

        self.window.columnconfigure(0, weight=2)
        self.window.columnconfigure(1, weight=3)
        self.window.columnconfigure(2, weight=4)
        self.window.columnconfigure(3, weight=2)
        
        self.assign_number()
        self.update_countdown()
        self.window.mainloop()

    def update_countdown(self):
        self.countdownText.config(text=str(self.countdownTime)+' sekund')
        if self.countdownTime > 0:
            if self.FOUND_STATUS:
                self.countdownTime -= 1
                self.window.after(1000, self.update_countdown)
            
        else:
            self.confirmbtn.config(state='disabled')
            messagebox.showerror("Time limit", "VAQT TUGADI!!!")
            self.FOUND_STATUS = 0
            self.window.destroy()
            
    def assign_number(self):
        self.NUMBER = randint(self.A, self.B)
        
    def check(self):
        value = int(self.mainEntry.get())
        if value > self.NUMBER:
            messagebox.showerror("Xato","Bu son men oylagan sondan katta. Qayta urinib ko'ring")
        elif value < self.NUMBER:
            messagebox.showerror("Xato","Bu son men o'ylagan sondan kichik. Qayta urinib ko'ring")
        else:
            self.FOUND_STATUS = 0
            self.countdownText.config(fg='green')
            messagebox.showinfo("Tabriklayman!", f"{value} men o'ylagan son edi. Siz buni topdingiz")
            if messagebox.askyesno("", "Yana o'ynaysizmi?"):
                self.window.after(300,self.window.destroy())
                GetRange()
            else: self.window.after(100, self.window.destroy())
            
class GetRange:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('300x300')
        self.window.title(TITLE)
        
        self.labelMain = tk.Label(self.window, text='Son oralig\'ini kiriting:', font=('Arial', 17)).pack()
        
        self.labelA = tk.Label(self.window, text='From:', font=('Arial', 16), pady=10)
        self.labelA.pack()
        
        self.entryA = tk.Entry(self.window, font=('Arial', 16), justify='center')
        self.entryA.pack()
        
        self.labelB = tk.Label(self.window, text='To:', font=('Arial', 16), pady=10)
        self.labelB.pack()
        
        self.entryB = tk.Entry(self.window, font=('Arial', 16), justify='center')
        self.entryB.pack()
        
        self.confirmbtn = tk.Button(self.window, text='Next', font=('Arial', 16), padx=10, pady=10, command=self.closeRange)
        self.confirmbtn.pack()
        
        self.window.mainloop()
        
    def closeRange(self):
        global A, B
        a = int(self.entryA.get())
        b = int(self.entryB.get())
        if a>=b:
            messagebox.showerror("Xatolik", "Noto'g'ri son oralig'i kiritildi")
            self.entryA.delete(0, 'end')
            self.entryB.delete(0, 'end')
        else:
            A = a
            B = b
            self.window.destroy()
            GetTime()

class GetTime:
    def __init__(self):
        self.time_window = tk.Tk()
        self.time_window.geometry('300x180')
        self.time_window.title(TITLE)

        self.labelT = tk.Label(self.time_window, text='Vaqtni kiriting', font=('Arial', 14), padx=10, pady=20)
        self.labelT.pack()
        
        self.entryT = tk.Entry(self.time_window, font=('Arial', 14), justify='center')
        self.entryT.pack()
        
        self.confirmbtn = tk.Button(self.time_window, text='Done', font=('Arial', 14), pady=10, command=self.closeTime)
        self.confirmbtn.pack()
        
        self.time_window.mainloop()
        
    def closeTime(self):
        global USERTIME
        USERTIME = int(self.entryT.get())
        self.time_window.destroy()
        Game()

class Welcome:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x400')
        self.window.title(TITLE)

        self.maintitle = tk.Label(self.window, text='Xush kelibsiz!', font=('Arial', 20), bg='white', padx=10, pady=10)
        self.maintitle.pack()

        self.welcometext = tk.Label(self.window, text=SHARTLAR, justify='left', font=('Arial', 16), bg='white', padx=20, pady=30)
        self.welcometext.pack()

        self.closebtn = tk.Button(self.window, text='OK', font=('aria', 16), command=self.start_game)
        self.closebtn.pack()

        self.window.mainloop()

    def start_game(self):
        self.window.destroy()
        GetRange()

Welcome()