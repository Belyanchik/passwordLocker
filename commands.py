import sqlite3
import webbrowser
from tkinter import *

database = sqlite3.connect("passwords.db")
cursor = database.cursor()

def openSourceCode():  #opening a repository on github
    webbrowser.open_new("https://github.com/Belyanchik/passwordLocker")

def addPasswordInBase(service, password, statusLabel):  #adding a password to the database
    newService = ""
    for i in range(len(service)):
        symbol = ord(service[i])
        symbol = symbol * 3
        newService = newService + str(chr(symbol))
    newPassword = ""
    for i in range(len(password)):
        symbol = ord(password[i])
        symbol = symbol * 5
        newPassword = newPassword + str(chr(symbol))

    cursor.execute(f"SELECT service FROM passwords WHERE service = '{newService}'")
    if(cursor.fetchone() == None):
        cursor.execute(f"INSERT INTO passwords VALUES (?, ?)", (newService, newPassword))
        database.commit()
        statusLabel["text"] = "Password added"
        statusLabel.place(x = 120, y = 220)
    else:
        cursor.execute(f"UPDATE passwords SET password = ? WHERE service = ?", (newPassword, newService))
        database.commit()
        statusLabel["text"] = "Password updated"
        statusLabel.place(x = 110, y = 220)

def getPasswordFromBase(service, statusGetLabel, forGetPassword):  #getting the password from the database
    newService = ""
    for i in range(len(service)):
        symbol = ord(service[i])
        symbol = symbol * 3
        newService = newService + str(chr(symbol))

    cursor.execute(f"SELECT service FROM passwords WHERE service = '{newService}'")
    if(cursor.fetchone() == None):
        statusGetLabel["text"] = "The password is missing"
        statusGetLabel.place(x = 85, y = 220)
    else:
        password = cursor.execute(f"SELECT password FROM passwords WHERE service = '{newService}'").fetchone()[0]
        newPassword = ""
        for i in range(len(password)):
            symbol = ord(password[i])
            symbol = symbol // 5
            newPassword = newPassword + str(chr(symbol))
        forGetPassword.delete(0, END)
        forGetPassword.insert(0, newPassword)
        statusGetLabel.place_forget()
