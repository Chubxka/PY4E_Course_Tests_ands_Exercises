lang=input('What is your language?')
def greet(lang):
    if lang=='es':
        return('Hola')
    elif lang=="it":
        return("Ciao")
    elif lang=="fr":
        return('Bonjour')
    else:
        return('Hello')

if lang=='es':
    name=input('Cómo te llamas?')
elif lang=='it':
    name=input('Come ti chiami?')
elif lang=='fr':
    name=input('Quel est ton nom?')
else:
    print('What is your name?')
print(greet(lang),name)