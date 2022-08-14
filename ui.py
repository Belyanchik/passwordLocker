from tkinter import *

import commands

def clearMenu():  #hide menu widgets
    addButton.place_forget()
    getButton.place_forget()
    codeButton.place_forget()

def backFromAdd():  #hide add widgets
    nameLabel.place_forget()
    forName.place_forget()
    passwordLabel.place_forget()
    forPassword.place_forget()
    addButton.place_forget()
    backButton.place_forget()
    statusLabel.place_forget()
    menu()

def backFromGet():  #hide get widgets
    nameGetLabel.place_forget()
    forGetName.place_forget()
    passwordGetLabel.place_forget()
    forGetPassword.place_forget()
    getButton.place_forget()
    backGetButton.place_forget()
    statusGetLabel.place_forget()
    menu()

def sendPassword():  #saving the password
    service = forName.get().lower()
    password = forPassword.get()
    if(service == "" or password == ""):
        statusLabel["text"] = "Not all fields are filled in"
        statusLabel.place(x = 90, y = 220)
    else:
        commands.addPasswordInBase(service, password, statusLabel)

def takePassword():  #getting a password
    service = forGetName.get().lower()
    if(service == ""):
        statusGetLabel["text"] = 'The "service" field is not filled in'
        statusGetLabel.place(x = 60, y = 220)
    else:
        commands.getPasswordFromBase(service, statusGetLabel, forGetPassword)

def menu():  #ui menu
    global addButton, getButton, codeButton
    title = Label()
    title["text"] = "Password Locker"
    title["font"] = "Arial 25"
    title.place(x = 75, y = 25)

    addButton = Button()
    addButton["text"] = "Add password"
    addButton["width"] = 30
    addButton["height"] = 2
    addButton["command"] = addPassword
    addButton.place(x = 85, y = 95)

    getButton = Button()
    getButton["text"] = "Get password"
    getButton["width"] = 30
    getButton["height"] = 2
    getButton["command"] = getPassword
    getButton.place(x = 85, y = 165)

    codeButton = Button()
    codeButton["text"] = "Source code"
    codeButton["width"] = 30
    codeButton["height"] = 2
    codeButton["command"] = commands.openSourceCode
    codeButton.place(x = 85, y = 230)

    versionLabel = Label()
    versionLabel["text"] = "by Belyanchik v1.0"
    versionLabel["font"] = "Arial 10"
    versionLabel.place(x = 280, y = 525)

def addPassword():  #ui add password
    global nameLabel, forName, passwordLabel, forPassword, addButton, backButton, statusLabel
    clearMenu()
    nameLabel = Label()
    nameLabel["text"] = "Enter the name of the service"
    nameLabel["font"] = "Arial 15"
    nameLabel.place(x = 70, y = 75)

    forName = Entry()
    forName["width"] = 28
    forName.place(x = 110, y = 115)

    passwordLabel = Label()
    passwordLabel["text"] = "Enter the password"
    passwordLabel["font"] = "Arial 15"
    passwordLabel.place(x = 107, y = 140)

    forPassword = Entry()
    forPassword["width"] = 28
    forPassword.place(x = 110, y = 180)

    addButton = Button()
    addButton["text"] = "Add"
    addButton["width"] = 30
    addButton["height"] = 2
    addButton["command"] = sendPassword
    addButton.place(x = 85, y = 425)

    backButton = Button()
    backButton["text"] = "Back"
    backButton["width"] = 30
    backButton["height"] = 2
    backButton["command"] = backFromAdd
    backButton.place(x = 85, y = 480)

    statusLabel = Label()
    statusLabel["font"] = "Arial 15"

def getPassword():  #ui get password
    global nameGetLabel, forGetName, passwordGetLabel, forGetPassword, getButton, backGetButton, statusGetLabel
    clearMenu()
    nameGetLabel = Label()
    nameGetLabel["text"] = "Enter the name of the service"
    nameGetLabel["font"] = "Arial 15"
    nameGetLabel.place(x = 70, y = 75)

    forGetName = Entry()
    forGetName["width"] = 28
    forGetName.place(x = 110, y = 115)

    passwordGetLabel = Label()
    passwordGetLabel["text"] = "Your password"
    passwordGetLabel["font"] = "Arial 15"
    passwordGetLabel.place(x = 125, y = 140)

    forGetPassword = Entry()
    forGetPassword["width"] = 28
    forGetPassword.place(x = 110, y = 180)

    getButton = Button()
    getButton["text"] = "Get"
    getButton["width"] = 30
    getButton["height"] = 2
    getButton["command"] = takePassword
    getButton.place(x=85, y=425)

    backGetButton = Button()
    backGetButton["text"] = "Back"
    backGetButton["width"] = 30
    backGetButton["height"] = 2
    backGetButton["command"] = backFromGet
    backGetButton.place(x=85, y=480)

    statusGetLabel = Label()
    statusGetLabel["font"] = "Arial 15"
