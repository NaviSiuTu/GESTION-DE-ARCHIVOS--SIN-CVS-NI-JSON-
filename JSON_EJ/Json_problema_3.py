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

def cargar_existente(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            if contenido:
                try:
                    return json.loads(contenido)
                except json.JSONDecodeError:
                    print("⚠️ El archivo existente tiene formato inválido. Se ignorará.")
    return {}

def main():
    ruta_base = os.path.dirname(__file__)
    ruta_entrada = os.path.join(ruta_base, "notas.json")
    ruta_salida = os.path.join(ruta_base, "promedio_estudiante.json")

    try:
        datos = leer_json(ruta_entrada)
    except Exception as e:
        print(str(e))
        return

    # Carga el archivo existente sin sobrescribir
    promedios = cargar_existente(ruta_salida)

    while True:
        estudiante = input("📘 Ingrese el código del estudiante (o 'salir' para terminar): ").strip()
        if estudiante.lower() == 'salir':
            break

        if estudiante not in datos:
            print(f"❌ El estudiante '{estudiante}' no existe en el archivo.")
            continue

        promedio = calcular_promedio(datos[estudiante])
        promedios[estudiante] = promedio
        print(f"✅ Promedio de {estudiante}: {promedio}")

    # Guardar todos los promedios actualizados
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            json.dump(promedios, f, indent=4, ensure_ascii=False)
        print(f"\n📁 Todos los promedios se guardaron en: {ruta_salida}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {str(e)}")

if __name__ == "__main__":
    main()

