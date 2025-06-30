# Importación de módulos necesarios
import tkinter as tk  # Para la interfaz gráfica
from tkinter import messagebox, filedialog  # Para ventanas emergentes y selección de archivos
import csv  # Para leer archivos CSV
import os  # Para trabajar con rutas de archivos

# -------------------------------
# FUNCIONES
# -------------------------------

def contar_compras_por_pago(nombre_archivo, medio_pago):
    
    # Cuenta cuántas compras se realizaron con un medio de pago específico en un archivo CSV.
    
    contador = 0
    try:
        # Abre el archivo CSV con codificación UTF-8
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Lee el archivo como diccionarios
            for fila in lector:
                if fila["Payment_Type"] == medio_pago:  # Compara el medio de pago
                    contador += 1  # Incrementa el contador si coincide
        return contador
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo no encontrado.")  # Si no se encuentra el archivo
    except KeyError:
        messagebox.showerror("Error", "La columna 'Payment_Type' no existe.")  # Si la columna no está
    return None

def buscar():
    
    # Ejecuta la búsqueda del medio de pago ingresado y muestra el resultado en pantalla.
    
    pago = entry_pago.get()
    if pago.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor, ingresa un medio de pago.")  # Si no se ingresó nada
        return
    
    if not ruta_archivo.get():
        messagebox.showwarning("Advertencia", "Por favor, selecciona el archivo CSV.")  # Si no se seleccionó archivo
        return

    resultado = contar_compras_por_pago(ruta_archivo.get(), pago)  # Ejecuta el conteo
    
    if resultado is not None:
        resultado_label.config(text=f"Compras realizadas con {pago}: {resultado}")  # Muestra el resultado

def seleccionar_archivo():
    
    # Abre un diálogo para seleccionar un archivo CSV desde el sistema de archivos.
    
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("CSV Files", "*.csv")]  # Solo permite seleccionar archivos .csv
    )
    if archivo:
        ruta_archivo.set(archivo)  # Guarda la ruta en la variable
        label_archivo.config(text=f"Archivo seleccionado:\n{os.path.basename(archivo)}")  # Muestra el nombre del archivo

# -------------------------------
# INTERFAZ GRÁFICA
# -------------------------------

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Compras por Medio de Pago")

# Variable para almacenar la ruta del archivo seleccionado
ruta_archivo = tk.StringVar()

# Etiqueta y entrada para el medio de pago
tk.Label(ventana, text="Ingresa el medio de pago:").pack(pady=5)
entry_pago = tk.Entry(ventana, width=40)
entry_pago.pack(pady=5)

# Botón para seleccionar archivo CSV
tk.Button(ventana, text="Seleccionar archivo CSV", command=seleccionar_archivo).pack(pady=5)

# Muestra el nombre del archivo seleccionado
label_archivo = tk.Label(ventana, text="Ningún archivo seleccionado", fg="gray")
label_archivo.pack(pady=2)

# Botón para ejecutar la búsqueda
tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)

# Etiqueta para mostrar resultados
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# -------------------------------
# INICIA EL PROGRAMA
# -------------------------------
ventana.mainloop()  # Bucle principal de Tkinter

