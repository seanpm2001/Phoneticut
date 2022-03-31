#!/usr/bin/env python
# Start of script
def main_en_us():
  print("Welcome to the Phoneticut client!")
  print("Record a new voice - ID: #nev")
  print("Listen to existing voie - ID: #exv")
  print("Exit")
  console1 = str(input("Enter an ID: ))
  console1 == console1.upper()
  if (console1 == "NEV" or "#NEV"):
    return compose_menu_en_us()
    break
  elif (console1 == "EXV" or "#EXV"):
    return menu1()
    break
  else:
    print("Invalid input")
    noMore = input("Press [ENTER] key to quit")
    break
def composeMenu_en_us()
  print("Compose a new voice set in:\n")
  print("Latin (English) - ID: #LatEN")
  print("Latin (Icelandic) - ID: #LatICE")
  print("Cyrillic (Ukrainian) - ID: #cyrUK")
  print("Cyrillic (Serbian) - ID: #cyrSB")
  print("Amharic - ID: #AMHAR")
  print("Arabic - ID: #Arabic")
  print("Greek - ID: #HelGK")
  print("")
  console2 = str(input("Enter an ID: "))
  console2 == console2.upper()
  if (console2 == "LATEN" or "#LATEN"):
    return compose_LATEN()
    break
  elif (console2 == "LATICE" or #LATICE"):
    return compose_LATICE()
    break
  elif (console2 == "CYRUK" or "#CYRUK"):
    return compose_CYRUK()"
    break
  elif (console2 == "CYRSB" or "#CYRSB"):
    return compose_CYRSB()
    break
  elif (console2 == "AMHAR" or "#AMHAR"):
    return compose_AMHAR()
    break
  elif (console2 == "ARABIC" or "#ARABIC"):
    return compose_ARABIC()
    break
  elif (console2 == "HELGK" or "#HELGK"):
    return compose_HELGK()
    break
  else:
    print("Invalid ID. Returning home...")
    return main_en_us()
    break
def compose_LATEN():
  print("")
  break
def about_en_us():
  print("About Phoneticut (Client) Alpha")
  print("Version 0.0.1 Alpha")
  print("Record just a few patterns of speech, and have a full voice actor replacement with a little synthesis")
  print("This project is licensed under the GNU General Public License V3")
  print("Development history: ID: #DEVHIS")
  consoleAB = str(input("Enter an ID, or type nonsense to exit: "))
  consoleAB == consoleAB.upper()
  if (consoleAB == "DEVHIS" or "#DEVHIS"):
    return about_dev_history_en_us()
    break
  else:
    return main_en_us()
    break
  break
def about_dev_history_en_us():
  print("Development history")
  print("I originally tried to write this client in CSound, but it proved impossible, so I tried Perl. It was a bit too difficult, so I went with Python")
  print("There is still a lot I want to do with this. A few corrections from what I did today include:")
  print("Better ID sets\nImproved language support\nMore language support\nA functional GUI, rather than a difficult CLI\nBetter menu text\nMore customizations\nA working product"
  break
return main_en_us()
return 0
break
""" File info
File type: Python source file (*.py)
File version: 1 (2022, Wednesday, March 30th at 11:00 pm)
Line count (including blank lines and compiler line): 90
"""
# End of script
