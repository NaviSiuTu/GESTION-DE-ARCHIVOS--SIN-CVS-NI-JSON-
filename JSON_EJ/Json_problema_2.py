import json
import os

def leer_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def encontrar_coincidencias(json1, json2):
    coincidencias = {}
    for clave in json1:
        if clave in json2 and json1[clave] == json2[clave]:
            coincidencias[clave] = json1[clave]
    return coincidencias

def main():
    ruta1 = os.path.join("JSON_EJ", "archivo1.json")
    ruta2 = os.path.join("JSON_EJ", "archivo2.json")
    salida = os.path.join("JSON_EJ", "coincidencias.json")

    datos1 = leer_json(ruta1)
    datos2 = leer_json(ruta2)

    coincidencias = encontrar_coincidencias(datos1, datos2)

    with open(salida, 'w', encoding='utf-8') as f:
        json.dump(coincidencias, f, indent=4, ensure_ascii=False)

    print(f"✅ Coincidencias guardadas en: {salida}")

if __name__ == "__main__":
    main()

