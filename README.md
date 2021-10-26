# googleShredder

Well this script is so dumb, actually it has no real purpose but *"entertaining"*.  
You insert a text, and it will use **google translate** to translate it through multiple languages to generate absolutely ridiculous texts. Here is how it works:  
it takes the sentence, and translates it to eg. French. Then it takes that French sentence and translates it to, let's say, Italian. And because of google translates skilled translation algorithms, and misinterpretations of some texts, very soon the text is destructed.  

**Installation**  
Info: You will need python3 and pip3 installed on you system.  
Info #2: Since on linux tkinter is not installed by default, the installer will try to apt-get it and therefor need superuser.  

You can either use `git clone https://github.com/DerBejijing/googleshredder` or download it as a zip.  
Next, you install the dependencies by running    
  - `installs.command` on linux / macOS  
  - `installs.bat` on windows  

After that you run the matching run file. Same here,  
  - `run.command` on linux / macOS  
  - `run.bat` on windows  

**How to use**  
Once you started the script a orange window will open. Insert a text of you choice in the upper field (also consider trying out a few random characters, very fun) and select your target language in the menubar. Next click on the cascade "Destruct" and choose between normal and complex mode. Complex mode takes a lot longer and you won't be able to recognize the original text again. But just try and see.  

**Good to know**  
  - Since the translation and the window handler are running in the same thread, during translation you will not be able to interact with the window. This will be changed in future versions. But to see if the programm is actually running, you can view its current status in the console.  
  - The time for a text to translate depends on your internet connection and the text length.  


**What you are (not) allowed to do**  
You are allowed to use, share and review this programm, as long as I am mentioned as the creator.  
You are allowed to modify the programm or use it in you own project, as long as I am mentioned as the original creator.  
