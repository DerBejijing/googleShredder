# googleShredder


Dieses Programm ist so dämlich, es hat eigentlich keinen Grund überhaupt zu existieren
Es nutzt Google-Translate um einen vorgegebenen Text durch einen Pfad an mehreren Sprachen zu übersetzen, bis
der Ursprüngliche Sinn nur noch schwer erkennbar ist.

Vorbereitung:
- benötigte Python Version: 3.x
- ausführen von der Installationsdatei der benötigten Bibliotheken:
  - Windows:  installs.bat
  - mac OS:   installs.command
  
  alternativ folgende Pakete über pip3 installieren:
  - pycountry
  - googletrans==4.0.0rc1
 
Nutzung:
- entweder ausführen der entsprechenden Start-Datei, oder Aufrufen von
  python3 <path>/src/shredder.py
  
- In der sich öffnenden Oberfläche befindet sich ein Input-Feld (oben).
  Dort geben Sie einen Text ihrer Wahl ein und klicken anschließend entweder auf
  "Text Schrotten" oder "Text komplex Schrotten".
  Der Text wird nun entweder durch einen festgelegten Pfad an Sprachen übersetzt oder durch alle bei
  google verfügbaren.
  Im terminal können Sie den aktuellen Fortschritt überwachen.
  
- nach einiger Zeit (abängig von Datendurchsatz der Internetverbindung) erscheint Ihr
  neuer Text im Terminal
  
  
Ja ähhh, haben Sie Spaß
