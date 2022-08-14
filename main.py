from tkinter import *
import sqlite3

import ui

database = sqlite3.connect("passwords.db")
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS passwords(
    service TEXT,
    password TEXT
)""")

root = Tk()

WIDTH = 400
HEIGHT = 550

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

root.title("Password Locker")
root.resizable(False, False)

ui.menu()

root.mainloop()
