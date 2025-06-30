import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os

def contar_compras_por_pago(nombre_archivo, medio_pago):
    contador = 0
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["Payment_Type"] == medio_pago:
                    contador += 1
        return contador
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo no encontrado.")
    except KeyError:
        messagebox.showerror("Error", "La columna 'Payment_Type' no existe.")
    return None

def buscar():
    pago = entry_pago.get()
    if pago.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor, ingresa un medio de pago.")
        return
    
    if not ruta_archivo.get():
        messagebox.showwarning("Advertencia", "Por favor, selecciona el archivo CSV.")
        return

    resultado = contar_compras_por_pago(ruta_archivo.get(), pago)
    
    if resultado is not None:
        resultado_label.config(text=f"Compras realizadas con {pago}: {resultado}")

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
ventana.title("Contador de Compras por Medio de Pago")

ruta_archivo = tk.StringVar()

# Widgets
tk.Label(ventana, text="Ingresa el medio de pago:").pack(pady=5)
entry_pago = tk.Entry(ventana, width=40)
entry_pago.pack(pady=5)

tk.Button(ventana, text="Seleccionar archivo CSV", command=seleccionar_archivo).pack(pady=5)

label_archivo = tk.Label(ventana, text="Ningún archivo seleccionado", fg="gray")
label_archivo.pack(pady=2)

tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Ejecutar
ventana.mainloop()
