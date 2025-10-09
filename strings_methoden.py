# print(dir(str)) # shows all string methods

# print("adem".zfill(10)) #000000adem, pads with zeros to length 10

# print("adem!".upper()) #ADEM!, converts to uppercase

# print("adem!".lower()) #adem!, converts to lowercase

# print("AdEm".lower()) #adem, makes all lowercase

# print("adem".capitalize()) #Adem, first letter uppercase

# print("adem".isupper()) #False, checks if all uppercase

# print("adem".islower()) #True, checks if all lowercase

# print("0176123123".isnumeric()) #True, checks if only numbers

# print("adem".isalpha()) #True, checks if only letters

# print("adem;ado;adolf;apo".split(';')) #['adem', 'ado', 'adolf', 'apo'], splits strings

# print("Adem\nAdo\nAdolf\nApo".splitlines()) #['Adem', 'Ado', 'Adolf', 'Apo']

# print("Adem\nAdo\nAdolf\nApo".split("\n")) #['Adem', 'Ado', 'Adolf', 'Apo']

# print("   Adem   ".strip()) #Adem, removes leading and trailing spaces

# print("   Ade   m   ".replace(" ", "")) #Adem, replaces all spaces with nothing

# print("   Adem   ".replace("em", "o" )) #Ado, replaces 'em' with 'o'

# print("BremerStadtMusikanten".count('e')) #3, counts occurrences of 'e'

# print("BremerStadtMusikanten".index('S')) #6, returns index of first 'S'

# print("BremerStadtMusikanten".index('o')) #ValueError, 'o' not found

# print("BremerStadtMusikanten".find('o')) #-1 (not found), returns -1 if not found

# print("Bremer" in "BremerStadtMusikanten") #True, checks if substring exists



# passwort1 = "abc123"
# passwort2 = "Pass Wort"
# passwort3 = "ultr4g3h31m "

# print(passwort1.upper()) # ABC123
# print(passwort2.lower()) #pass wort
# print(passwort3.islower()) #True
# print(passwort2.isupper()) #False
# print(passwort1.zfill(8)) #00abc123
# print(passwort2.strip()) #Pass Wort
# print((len(passwort3))) #12
# print(passwort1.isalpha()) #False
# print(passwort1[3:].isnumeric()) #True
# print("a;b;c;d;e".split(';')) #['a','b','c','d','e']
# print("01.23.45.67.89".split(';')) #['01.23.45.67.89']
# print(passwort2.replace("Pass", '.')) # . Wort
# print(passwort3.count('3')) #2
# print(passwort2.count('s')) #2
# print(passwort3.find(2+2)) # TypeError
# print(passwort1.index("4")) #IndexError



# print("passw0r7"[:3].upper())                               # PASSw0r7
# print("Anime".zfill(11))                                    # 000000Anime
# print("adem".capitalize)                                    # Adem
# print("Gon".lower)                                          # gon
# print("0123456789"[:: -1])                                  # 9876543210