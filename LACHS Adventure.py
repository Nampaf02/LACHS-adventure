# Name = ""
# Autoren = Pawel & Jannis

from Spieler import Spieler
import random
import time
import cmd
import textwrap
import os
import sys

screen_width = 100

### Title Screen ###
def titel_screen_auswahl():
    option = input("> ")
    print("Benutze einen gueltigen Befehl.")
    if option.lower() == ("spielen"):
        spiel_starten() # Platzhalter für Funktion Spiel Starten!
    elif option.lower() == ("hilfe"):
        hilfe_screen()
    elif option.lower() == ("menu"):
        titel_screen()
    elif option.lower() == ("verlassen"):
        sys.exit()
    while option.lower() not in ['spielen', 'hilfe', 'verlassen']:
        print("Benutze einen gueltigen Befehl.")
        option = input("> ")
        if option.lower() == ("spielen"):
            spiel_starten() # Platzhalter für Funktion Spiel Starten!
        elif option.lower() == ("hilfe"):
            hilfe_screen()
        elif option.lower() == ("menu"):
            titel_screen()
        elif option.lower() == ("verlassen"):
            sys.exit()

def titel_screen():
    print("\n" * 100)
    print('####################################################')
    print('######           Wilkommen im LACHS           ######')
    print('####################################################')
    print('                    -  Spielen  -                   ')
    print('                    -   Hilfe   -                   ')
    print('                    - Verlassen -                   ')
    print('         Copyright 2019 LACHS Entertainment         ')
    print('             Wo der LACHS noch Loopt ALLA           ')
    titel_screen_auswahl()

def hilfe_screen():
    print("\n" * 100)
    print('######################################################')
    print('######           Wilkommen im LACHS           ########')
    print('######################################################')
    print('#Benutze Hoch   | North um dich nach oben zu bewegen #')
    print('#Benutze Rechts | East um dich nach Rechts zu bewegen#')
    print('#Benutze Unten  | South um dich nach Unten zu bewegen#')
    print('#Benutze Links  | East um dich nach Links zu bewegen #')
    print('# Benutze das Textfeld um deinen Befehl auszufuehren #')
    print('#  Benutze den Befehl Menu um wieder zurückzukehren  #')   
    print('######################################################')
    print('         Copyright 2019 LACHS Entertainment           ')
    print('             Wo der LACHS noch Loopt ALLA             ')
    titel_screen_auswahl()

titel_screen()
