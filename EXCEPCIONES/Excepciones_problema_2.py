def operar(a, b):
    return a + b

def main():
    try:
        a = int(input("🔢 Ingrese un número: "))
        b = 'hola'
        resultado = operar(a, b)
        print("Resultado:", resultado)
    
    except ValueError:
        print("❌ Lo que ingresaste no es un número válido.")
    
    except TypeError:
        print("❌ Los tipos de datos no cuadran para hacer la operación.")

main()


#--------- sin except ----------

def operar(a, b):
    return a + b

def main():
    a = int(input())  # Usuario digita un número válido (por ejemplo, 5)
    b = 'hola'
    operar(a, b)      # 💥 Aquí explota: no se puede sumar int + str

main()
