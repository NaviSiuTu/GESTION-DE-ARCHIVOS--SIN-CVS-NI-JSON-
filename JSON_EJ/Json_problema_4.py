# Importamos los módulos necesarios
import json  # Para manejar archivos JSON
import os    # Para trabajar con rutas y verificar existencia de archivos

# Diccionario que define cómo reemplazar los caracteres encriptados por letras reales
DECODIFICACION = {
    '$': 'a',
    '#': 'e',
    '*': 'i',
    '¬': 'o',
    '+': 'u'
}

# Función para leer un archivo JSON desde una ruta dada
def leer_json(ruta):
    # Verifica si el archivo existe
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta}")
    
    # Abre el archivo y lo lee
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        # Si el archivo está vacío, lanza un error
        if not contenido:
            raise ValueError(f"❌ El archivo {ruta} está vacío")
        # Convierte el contenido del archivo de texto a un diccionario
        return json.loads(contenido)

# Función para desencriptar un texto usando el diccionario DECODIFICACION
def desencriptar_texto(texto):
    # Reemplaza cada carácter según el diccionario, o lo deja igual si no está codificado
    return ''.join(DECODIFICACION.get(c, c) for c in texto)

# Función principal del programa
def main():
    # Define las rutas relativas al archivo actual
    ruta_base = os.path.dirname(__file__)
    ruta_entrada = os.path.join(ruta_base, "encriptado.json")       # Archivo de entrada (encriptado)
    ruta_salida = os.path.join(ruta_base, "desencriptado.json")     # Archivo de salida (desencriptado)

    # Intenta leer el archivo encriptado
    try:
        datos = leer_json(ruta_entrada)
    except Exception as e:
        print(str(e))
        return

    # Crea un nuevo diccionario con los textos ya desencriptados
    desencriptado = {
        clave: desencriptar_texto(valor)
        for clave, valor in datos.items()
    }

    # Intenta guardar el resultado en un nuevo archivo JSON
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(desencriptado, f, indent=4, ensure_ascii=False)
        print(f"✅ Desencriptado guardado en: {ruta_salida}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {str(e)}")

# Ejecuta la función main solo si este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()

