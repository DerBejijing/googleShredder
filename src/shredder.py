from tkinter import *
from googletrans import Translator
from os import name, system
import pycountry
import sys
import math

trPath = ['']
progress = 0

tr = Translator()
print("[*] Starting...")

def progressBar(currentPosition):
    global progress
    totalItems = len(trPath)
    return math.floor(((currentPosition) / totalItems) * 100)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def trashText():
    textToTranslate = str(InputText.get("1.0",END))
    print(trPath)
    for lang in trPath:
        try:
            text = tr.translate(textToTranslate, dest=lang)
            textToTranslate = text.text
        except Exception as e:
            pass

        clear()
        print("[*] Progress: " + str(progressBar(trPath.index(lang))) + "%")

    clearOut()
    OutputText.insert(END, textToTranslate)
    clear()
    print("[*] Progress: 100%")
    print("[*] done!")

def trashTextNormal():
    print("[*] using normal destruction mode")
    global trPath
    trPath = ['ar','la','ja','de']
    trashText()


def trashTextComplex():
    print("[*] using complex destruction mode")
    global trPath
    trPath = ['']
    try:
        for country in pycountry.countries:
            trPath.append(str.lower(country.alpha_2))
    except Exception as e:
        print("")
        print("[!] Error occured whilst generating translation path!")
        print("[!] Make sure to have module 'pycountry' installed!")
        print("[!] If the error remains, please contact the developer")


    print("[*] Path generated!")
    trPath = list(dict.fromkeys(trPath))
    trPath.remove('de')
    trPath.append('de')

    trashText()

def clearOut():
    OutputText.delete("1.0", END)

def clearAll():
    OutputText.delete("1.0", END)
    InputText.delete("1.0", END)

def quitProgramm():
    sys.exit(0)

window = Tk()
window.title("Enhance your understanding of grammar")
window.config(bg="orange red")

InfoLabel = Label(window, text="Enhance your knowledge about grammar", anchor=W, justify=LEFT, bg="orange red", fg= "white", font="none 24 bold").grid(row=0,column=0)
DescLabel = Label(window, text="Gib hier einen (grammatikalisch korrekten, DEUTSCHEN) Text ein:", anchor=W, justify=LEFT, bg="orange red", fg="white", font="none 12 bold").grid(row=1,column=0)
InputText = Text(window, height=10, width=50)
InputText.grid(row=2,column=0)
line1 = Label(window, text="\n\n").grid(row=3,column=0)
trashButton = Button(window, text="Text Schrotten", command=trashTextNormal).grid(row=4,column=0)
trashButtonComplex = Button(window, text="Text Komplex Schrotten", command=trashTextComplex).grid(row=5,column=0)
clearButton = Button(window, text="Löschen", command=clearAll).grid(row=6,column=0)
line2 = Label(window, text="\n\n").grid(row=7,column=0)
OutputText = Text(window, height=10, width=50)
OutputText.grid(row=8,column=0)
nothing = Label(window, text="\n\n\n", bg="orange red", fg="orange red").grid(row=9,column=0)

quitButton = Button(window, text="Exit", bg="red", fg="black", command=quitProgramm).grid(row=10,column=0)


window.mainloop()
