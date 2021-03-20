from tkinter import *
from googletrans import Translator
from os import name, system
import pycountry
import sys
import math
import time

path = ['']
progress = 0
target_language = 'de'

def progressBar(currentPosition):
    global progress
    totalItems = len(path)
    return math.floor(((currentPosition) / totalItems) * 100)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def trashText():
    textToTranslate = str(InputText.get("1.0",END))
    print(path)
    for lang in path:
        try:
            text = tr.translate(textToTranslate, dest=lang)
            textToTranslate = text.text
        except Exception as e:
            pass

        clear()
        print("[*] Progress: " + str(progressBar(path.index(lang))) + "%")

    clearOut()
    OutputText.insert(END, textToTranslate)
    clear()
    print("[*] Progress: 100%")
    print("[*] done!")

def trashTextNormal():
    print("[*] using normal destruction mode")
    global path
    path = ['ar','la','ja']
    path.append(target_language)
    trashText()

def trashTextComplex():
    print("[*] using complex destruction mode")
    global path
    path = ['']
    try:
        for country in pycountry.countries:
            path.append(str.lower(country.alpha_2))
    except Exception as e:
        raise

    print("[*] Path generated!")
    path = list(dict.fromkeys(path))
    try:
        path.remove(target_language)
    except Exception as e:
        pass

    path.append(target_language)
    trashText()

def clearOut():
    OutputText.delete("1.0", END)

def clearAll():
    OutputText.delete("1.0", END)
    InputText.delete("1.0", END)

def quitProgramm():
    sys.exit(0)

def setTargetLang(language):
    global target_language
    target_language = language
    OutputLabel.config(text="Output (" + language + "):")
    print("[*] Target language changed to: " + language)

def help():
    print("[*] Helping")

tr = Translator()
print("[*] Starting")

window = Tk()
menu = Menu(window)
window.title("Enhance your understanding of grammar")
window.config(bg="orange red")
window.config(menu=menu)
window.resizable(False, False)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)

editMenu.add_command(label="clear fields", command=clearAll)
editMenu.add_command(label="help...", command=help)
editMenu.add_separator()
editMenu.add_command(label="quit", command=quitProgramm)

targetMenu = Menu(menu)
menu.add_cascade(label="target language", menu=targetMenu)

targetMenu.add_command(label="English (en)", command= lambda: setTargetLang("en"))
targetMenu.add_command(label="Deutsch (de)", command= lambda: setTargetLang("de"))
targetMenu.add_command(label="Français (fr)", command= lambda: setTargetLang("fr"))
targetMenu.add_command(label="Español (es)", command= lambda: setTargetLang("es"))

destructMenu = Menu(menu)
menu.add_cascade(label="destruct", menu=destructMenu)

destructMenu.add_command(label="Normal", command=trashTextNormal)
destructMenu.add_command(label="Complex", command=trashTextComplex)

InfoLabel = Label(window, text="Enhance your knowledge about grammar", anchor=W, justify=LEFT, bg="orange red", fg="white", font="none 24 bold").grid(row=0,column=0)
DescLabel = Label(window, text="Enter some text:", anchor=W, justify=LEFT, bg="orange red", fg="white", font="none 12 bold").grid(row=1,column=0)
InputText = Text(window, height=10, width=50)
InputText.grid(row=2,column=0)
OutputLabel = Label(window, text="Output (" + target_language + "):", anchor=W, justify=LEFT, bg="orange red", fg="white", font="none 12 bold")
OutputLabel.grid(row=3,column=0)
OutputText = Text(window, height=10, width=50)
OutputText.grid(row=4,column=0)
nothing = Label(window, text="\n\n\n", bg="orange red", fg="orange red").grid(row=5,column=0)
quitButton = Button(window, text="Exit", bg="red", fg="black", command=quitProgramm).grid(row=6,column=0)

window.mainloop()
