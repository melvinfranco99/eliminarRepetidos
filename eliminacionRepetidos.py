import tkinter as tk
from tkinter import filedialog
import pandas as pd

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx")])
    if archivo:
        entrada_archivo.delete(0, tk.END)
        entrada_archivo.insert(0, archivo)
        mostrar_tabla(archivo)

def mostrar_tabla(archivo):
    # Leer el archivo de Excel
    df = pd.read_excel(archivo)

    # Eliminar filas con valores 'nan'
    df = df.dropna()

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Crear una tabla en la interfaz
    tabla = tk.Frame(root)
    tabla.pack()

    # Agregar encabezados de columna
    for col in df.columns:
        label = tk.Label(tabla, text=col, relief="groove", padx=10, pady=5)
        label.grid(row=0, column=df.columns.tolist().index(col))

    # Agregar datos de la tabla
    for i, row in df.iterrows():
        for j, value in enumerate(row):
            entry = tk.Entry(tabla, width=20)
            entry.grid(row=i+1, column=j)
            entry.insert(0, str(value))

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Aplicación")

# Crear un label
label = tk.Label(root, text="Selecciona un archivo de Excel:")
label.pack()

# Crear una entrada de texto para mostrar la ruta del archivo
entrada_archivo = tk.Entry(root)
entrada_archivo.pack()

# Crear un botón para abrir el diálogo de selección de archivo
boton_seleccionar = tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()

# Iniciar el bucle de eventos
root.mainloop()
