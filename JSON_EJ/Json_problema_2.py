# Importar los módulos necesarios
import json  # Para trabajar con archivos JSON
import os    # Para trabajar con rutas de archivos

# Función para leer un archivo JSON y devolver su contenido como diccionario
def leer_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

# Función que encuentra las claves y valores que coinciden entre dos diccionarios
def encontrar_coincidencias(json1, json2):
    coincidencias = {}
    for clave in json1:
        # Si la clave también está en el segundo JSON y el valor es igual
        if clave in json2 and json1[clave] == json2[clave]:
            coincidencias[clave] = json1[clave]  # Agregarla a las coincidencias
    return coincidencias

# Función principal del programa
def main():
    # Definir rutas a los archivos de entrada y salida
    ruta1 = os.path.join("JSON_EJ", "archivo1.json")
    ruta2 = os.path.join("JSON_EJ", "archivo2.json")
    salida = os.path.join("JSON_EJ", "coincidencias.json")

    # Leer los archivos JSON
    datos1 = leer_json(ruta1)
    datos2 = leer_json(ruta2)

    # Encontrar claves y valores iguales entre ambos JSON
    coincidencias = encontrar_coincidencias(datos1, datos2)

    # Guardar el resultado en un nuevo archivo JSON
    with open(salida, 'w', encoding='utf-8') as f:
        json.dump(coincidencias, f, indent=4, ensure_ascii=False)

    # Mostrar mensaje de éxito
    print(f"✅ Coincidencias guardadas en: {salida}")

# Ejecutar el programa
if __name__ == "__main__":
    main()


