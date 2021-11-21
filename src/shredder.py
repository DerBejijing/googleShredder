from tkinter import *
from googletrans import Translator
from os import name, system
import pycountry
import sys
import math

# Came back to comment my many years-old beginner code.. what a pain to read...
# this is about to be recreated from the ground up

path = ['']
progress = 0
target_language = 'de'

# calculates a percentage value to indicate the progress of the translation process
# very misleading, it does not even display a progress-bar
def progressBar(currentPosition):
    totalItems = len(path)
    return math.floor(((currentPosition) / totalItems) * 100)

# clears the console window by running the platform-specific command
# cls for windows
# clear for mac / Linux
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# takes the value from the input field and translates it through all languages in the "path" array
# if a language is unsupported it gets skipped
def trashText():
    # get input-field value
    textToTranslate = str(InputText.get("1.0", END))
    
    # iterate through path-array
    for lang in path:
        try:
            # translate the text
            text = tr.translate(textToTranslate, dest=lang)
            textToTranslate = text.text
        except Exception as e:
            # pass if language is not available or invalid
            pass

        # clear console window
        clear()
        
        # update progress-indicator
        print("[*] Progress: " + str(progressBar(path.index(lang))) + "%")

    # clear the output field and insert final text
    clearOut()
    OutputText.insert(END, textToTranslate)
    
    # clear console window and print some text
    clear()
    print("[*] Progress: 100%")
    print("[*] Done!")

    
# generate a path with four languages and start translating
# uses "ar", "la", "ja" and the final language
def trashTextNormal():
    print("[*] Using normal destruction mode")
    global path
    path = ['ar','la','ja']
    path.append(target_language)
    
    # start translating
    trashText()

# generate a complex path using all languages and start translating
# appends the final language and removes the first occurence of it
# that is because of the stupid way I used to calculate the progress
def trashTextComplex():
    print("[*] Using complex destruction mode")
    global path
    path = ['']
    try:
        # iterate over all available languages pycountry offers and append their ISO 3166-1 alpha-2 code
        # the actual google-translate website uses other codes. Thus, I don't even know whether or not this works
        # once again, about to be remade
        for country in pycountry.countries:
            path.append(str.lower(country.alpha_2))
    except Exception as e:
        raise

    print("[*] Path generated!")
    
    # remove duplicates
    path = list(dict.fromkeys(path))
    try:
        path.remove(target_language)
    except Exception as e:
        pass

    # append target language and start translating
    path.append(target_language)
    trashText()

# clear the output field by deleting all characters
def clearOut():
    OutputText.delete("1.0", END)

# clear both fields by deleting all characters
def clearAll():
    OutputText.delete("1.0", END)
    InputText.delete("1.0", END)

# quit the program
# misspelled and dumb
def quitProgramm():
    sys.exit(0)

# change the text of the output-language label
def setTargetLang(language):
    global target_language
    target_language = language
    OutputLabel.config(text="Output (" + language + "):")
    print("[*] Target language changed to: " + language)

# prints help
def help():
    print("[*] README.md: github.com/DerBejijing/googleShredder")

# create a Translator-instance
tr = Translator()
print("[*] Starting")

# create the window and all items
window = Tk()
menu = Menu(window)
window.title("Enhance your understanding of grammar")
window.config(bg="orange red")
window.config(menu=menu)
window.resizable(False, False)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Clear fields", command=clearAll)
editMenu.add_command(label="Help...", command=help)
editMenu.add_separator()
editMenu.add_command(label="Quit", command=quitProgramm)

targetMenu = Menu(menu)
menu.add_cascade(label="Target language", menu=targetMenu)

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

# run until terminated
window.mainloop()
