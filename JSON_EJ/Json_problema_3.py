import json
import os

def leer_json(ruta):
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta}")
    
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            raise ValueError(f"❌ El archivo {ruta} está vacío")
        return json.loads(contenido)

def calcular_promedio(lista):
    if not lista:
        return 0.0
    return round(sum(lista) / len(lista), 2)

def main():
    # Ruta al archivo de entrada y salida
    ruta_base = os.path.dirname(__file__)
    ruta_entrada = os.path.join(ruta_base, "notas.json")
    ruta_salida = os.path.join(ruta_base, "promedio_estudiante.json")

    try:
        datos = leer_json(ruta_entrada)
    except Exception as e:
        print(str(e))
        return

    # Pedir código del estudiante
    estudiante = input("📘 Ingrese el código del estudiante (ej: A003): ").strip()

    if estudiante not in datos:
        print(f"❌ El estudiante '{estudiante}' no existe en el archivo.")
        return

    promedio = calcular_promedio(datos[estudiante])

    resultado = {estudiante: promedio}

    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=4, ensure_ascii=False)
        print(f"✅ Promedio guardado en: {ruta_salida}")
        print(f"📊 {estudiante}: {promedio}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {str(e)}")

if __name__ == "__main__":
    main()

