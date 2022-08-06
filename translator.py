from googletrans import Translator

translate = input('Enter Word/Sentence...\n')
tclass = Translator()

# language = 'it' # Translates to Italian
# language = 'kn'  # Translates to Kannada

print("****Select Language Code from the Menu**** \n")
print("1. English")
print("2. Hindi")
print("3. Italian")
print("4. Kannada")
print("5. Tamil")
print("6. Telugu")
print("7. Urdu")
print("8. Exit\n")

language = int(input("Select the Code: "))
lg = ''

while(True):
    if language == 1:
        lg = 'en'
        break
    elif language == 2:
        lg = 'hi'
        break
    elif language == 3:
        lg = 'it'
        break
    elif language == 4:
        lg = 'kn'
        break
    elif language == 5:
        lg = 'ta'
        break
    elif language == 6:
        lg = 'te'
        break
    elif language == 7:
        lg = 'ur'
        break
    elif language == 8:
        break



tlation = tclass.translate(translate, dest=lg)
print()
print(tlation.text)