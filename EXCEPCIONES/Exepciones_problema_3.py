#----- CON TRY EXCEPT --------

def main():
    lenguajes = {
        'James': 'Java',
        'Dennis': 'C',
        'Das': 'Python'
    }

    try:
        print(lenguajes['Ada'])
    except KeyError:
        print("❌ Intenta acceder una llave que no está en el diccionario. (Tienes que corregir)")

main()


#------ SIN TRY EXCEPT ------
def main():
    lenguajes = {
        'James': 'Java',
        'Dennis': 'C',
        'Das': 'Python'
    }
    
    # Esto provocará un error porque 'Ada' no está en el diccionario
    print(lenguajes['Ada'])

main()

