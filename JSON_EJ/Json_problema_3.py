# Importamos módulos necesarios
import json  # Para manejar archivos JSON
import os    # Para trabajar con rutas de archivo

# Función para leer el archivo JSON de entrada
def leer_json(ruta):
    # Verifica que el archivo exista
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta}")
    
    # Lee el archivo y verifica que no esté vacío
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            raise ValueError(f"❌ El archivo {ruta} está vacío")
        return json.loads(contenido)  # Convierte el texto JSON a diccionario

# Función para calcular el promedio de una lista de números
def calcular_promedio(lista):
    if not lista:
        return 0.0
    return round(sum(lista) / len(lista), 2)

# Función para cargar el archivo de promedios ya existentes (si existe)
def cargar_existente(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            if contenido:
                try:
                    return json.loads(contenido)
                except json.JSONDecodeError:
                    print("⚠️ El archivo existente tiene formato inválido. Se ignorará.")
    return {}  # Si no existe o está vacío, devuelve diccionario vacío

# Función principal
def main():
    # Rutas al archivo de entrada y al de salida
    ruta_base = os.path.dirname(__file__)
    ruta_entrada = os.path.join(ruta_base, "notas.json")
    ruta_salida = os.path.join(ruta_base, "promedio_estudiante.json")

    # Intenta leer el archivo de notas
    try:
        datos = leer_json(ruta_entrada)
    except Exception as e:
        print(str(e))
        return

    # Cargar promedios ya guardados (para no sobrescribir)
    promedios = cargar_existente(ruta_salida)

    # Bucle para ingresar estudiantes
    while True:
        estudiante = input("📘 Ingrese el código del estudiante (o 'salir' para terminar): ").strip()
        if estudiante.lower() == 'salir':
            break

        # Verifica que el estudiante exista en los datos
        if estudiante not in datos:
            print(f"❌ El estudiante '{estudiante}' no existe en el archivo.")
            continue

        # Calcula el promedio y lo guarda
        promedio = calcular_promedio(datos[estudiante])
        promedios[estudiante] = promedio
        print(f"✅ Promedio de {estudiante}: {promedio}")

    # Guardar todos los promedios al final
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(promedios, f, indent=4, ensure_ascii=False)
        print(f"\n📁 Todos los promedios se guardaron en: {ruta_salida}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {str(e)}")

# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    main()


