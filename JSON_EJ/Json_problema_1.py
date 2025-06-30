import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

class BuscadorDeportistas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Búsqueda de Deportistas")
        self.root.geometry("500x500")
        self.usuarios = self.cargar_datos()
        self.crear_interfaz()
    
    def cargar_datos(self):
        # Carga desde la carpeta JSON_EJ, sin importar desde dónde se ejecute el script
        ruta_base = os.path.dirname(__file__)
        ruta_json = os.path.join(ruta_base, "usuarios.json")
        print(f"[DEBUG] Cargando archivo desde: {ruta_json}")  # Línea de depuración

        try:
            with open(ruta_json, encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{str(e)}")
            exit()
    
    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Sistema de Búsqueda de Deportistas", 
                 font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        search_frame = ttk.LabelFrame(main_frame, text="Opciones de Búsqueda", padding="10")
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Buscar por deporte:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.deporte_entry = ttk.Entry(search_frame, width=25)
        self.deporte_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(search_frame, text="Buscar", command=self.buscar_deporte).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(search_frame, text="Buscar por edad:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.edad_frame = ttk.Frame(search_frame)
        self.edad_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.edad_frame, text="De").pack(side=tk.LEFT)
        self.edad_min_entry = ttk.Entry(self.edad_frame, width=5)
        self.edad_min_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(self.edad_frame, text="a").pack(side=tk.LEFT)
        self.edad_max_entry = ttk.Entry(self.edad_frame, width=5)
        self.edad_max_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Buscar", command=self.buscar_edad).grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Separator(main_frame, orient='horizontal').pack(fill=tk.X, pady=10)
        ttk.Label(main_frame, text="Resultados", font=('Helvetica', 12)).pack()
        
        self.resultados_text = tk.Text(main_frame, height=15, wrap=tk.WORD)
        self.resultados_text.pack(fill=tk.BOTH, expand=True, pady=5)
        scrollbar = ttk.Scrollbar(self.resultados_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.resultados_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.resultados_text.yview)
        
        ttk.Button(main_frame, text="Generar JSON de Deportes", 
                  command=self.generar_json_deportes).pack(pady=10)
    
    def buscar_deporte(self):
        deporte = self.deporte_entry.get().strip().title()
        if not deporte:
            messagebox.showwarning("Advertencia", "Por favor ingrese un deporte")
            return
        
        resultados = []
        for username, datos in self.usuarios.items():
            if deporte in [d.title() for d in datos.get("deportes", [])]:
                nombre_completo = f"{datos.get('nombres', '')} {datos.get('apellidos', '')}".strip()
                if nombre_completo:
                    resultados.append(nombre_completo)
        
        self.mostrar_resultados(resultados, f"Personas que practican {deporte}")
    
    def buscar_edad(self):
        try:
            edad_min = int(self.edad_min_entry.get())
            edad_max = int(self.edad_max_entry.get())
            
            if edad_min > edad_max:
                edad_min, edad_max = edad_max, edad_min
            
            resultados = []
            for username, datos in self.usuarios.items():
                edad_cruda = datos.get("edad")
                try:
                    edad = int(edad_cruda)
                except (ValueError, TypeError):
                    continue

                if edad_min <= edad <= edad_max:
                    nombre_completo = f"{datos.get('nombres', '')} {datos.get('apellidos', '')}".strip()
                    if nombre_completo:
                        resultados.append(nombre_completo)
            
            self.mostrar_resultados(resultados, f"Personas entre {edad_min} y {edad_max} años")
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para las edades")
    
    def generar_json_deportes(self):
        deportes_dict = {}
        
        for username, datos in self.usuarios.items():
            for deporte in datos.get("deportes", []):
                deporte = deporte.title()
                if deporte not in deportes_dict:
                    deportes_dict[deporte] = []
                deportes_dict[deporte].append(username)
        
        ruta_base = os.path.dirname(__file__)
        ruta_salida = os.path.join(ruta_base, "deportes.json")
        
        try:
            with open(ruta_salida, 'w', encoding='utf-8') as f:
                json.dump(deportes_dict, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Éxito", f"Archivo 'deportes.json' creado en:\n{ruta_salida}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el archivo:\n{str(e)}")
    
    def mostrar_resultados(self, resultados, titulo):
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)
        
        self.resultados_text.insert(tk.END, f"{titulo}\n")
        self.resultados_text.insert(tk.END, "="*len(titulo) + "\n\n")
        
        if resultados:
            for persona in resultados:
                self.resultados_text.insert(tk.END, f"• {persona}\n")
            self.resultados_text.insert(tk.END, f"\nTotal encontrados: {len(resultados)}")
        else:
            self.resultados_text.insert(tk.END, "No se encontraron resultados")
        
        self.resultados_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorDeportistas(root)
    root.mainloop()



