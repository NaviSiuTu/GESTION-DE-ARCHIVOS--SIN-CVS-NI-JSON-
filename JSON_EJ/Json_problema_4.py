import json
import os

# Diccionario de desencriptación
DECODIFICACION = {
    '$': 'a',
    '#': 'e',
    '*': 'i',
    '¬': 'o',
    '+': 'u'
}

def leer_json(ruta):
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta}")
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            raise ValueError(f"❌ El archivo {ruta} está vacío")
        return json.loads(contenido)

def desencriptar_texto(texto):
    return ''.join(DECODIFICACION.get(c, c) for c in texto)

def main():
    ruta_base = os.path.dirname(__file__)
    ruta_entrada = os.path.join(ruta_base, "encriptado.json")
    ruta_salida = os.path.join(ruta_base,"desencriptado.json")

    try:
        datos = leer_json(ruta_entrada)
    except Exception as e:
        print(str(e))
        return

    desencriptado = {
        clave: desencriptar_texto(valor)
        for clave, valor in datos.items()
    }

    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(desencriptado, f, indent=4, ensure_ascii=False)
        print(f"✅ Desencriptado guardado en: {ruta_salida}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {str(e)}")

if __name__ == "__main__":
    main()
