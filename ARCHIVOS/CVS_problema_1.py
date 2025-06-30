import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os

def contar_compras_por_pais(nombre_archivo, pais_dado):
    contador = 0
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["Country"] == pais_dado:
                    contador += 1
        return contador
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo no encontrado.")
    except KeyError:
        messagebox.showerror("Error", "La columna 'Country' no existe en el archivo.")
    return None

def buscar():
    pais = entry_pais.get()
    if pais.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor, ingresa un país.")
        return
    
    if not ruta_archivo.get():
        messagebox.showwarning("Advertencia", "Por favor, selecciona el archivo CSV.")
        return
    
    resultado = contar_compras_por_pais(ruta_archivo.get(), pais)
    
    if resultado is not None:
        resultado_label.config(text=f"Compras realizadas en {pais}: {resultado}")

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("CSV Files", "*.csv")]
    )
    if archivo:
        ruta_archivo.set(archivo)
        label_archivo.config(text=f"Archivo seleccionado:\n{os.path.basename(archivo)}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Contador de Compras por País")

ruta_archivo = tk.StringVar()

# Widgets
tk.Label(ventana, text="Ingresa el país:").pack(pady=5)
entry_pais = tk.Entry(ventana, width=40)
entry_pais.pack(pady=5)

tk.Button(ventana, text="Seleccionar archivo CSV", command=seleccionar_archivo).pack(pady=5)

label_archivo = tk.Label(ventana, text="Ningún archivo seleccionado", fg="gray")
label_archivo.pack(pady=2)

tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Ejecutar
ventana.mainloop()

