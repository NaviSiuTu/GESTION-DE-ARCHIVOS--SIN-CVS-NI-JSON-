# Lista de ejemplo
lista = [1, 2, 3, 4]

try:
    # Intento acceder a la posición 5 (índice inválido)
    print(lista[5])
except IndexError:
    print("❌ Intenta acceder a una posición que no está en el arreglo.")
