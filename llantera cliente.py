import tkinter as tk
from tkinter import ttk, messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú de Compra")
ventana.geometry("400x600")
ventana.configure(bg="#F0F8FF")  # Fondo azul muy suave

# Variables
tipo_carro = tk.StringVar()
tipo_llanta = tk.StringVar()
marca = tk.StringVar()
modelo_llanta = tk.StringVar()
campos = {}

# Función para mostrar resumen
def mostrar_resumen():
    resumen = f"""
Tipo de carro: {tipo_carro.get()}
Tipo de llanta: {tipo_llanta.get()}
Marca: {marca.get()}
Modelo de llanta: {modelo_llanta.get()}
Tamaño: {campos['Tamaño'].get()}
Anchura: {campos['Anchura'].get()}
Alto: {campos['Alto'].get()}
"""
    messagebox.showinfo("Resumen de la compra", resumen)

# Estilos
style = ttk.Style()
style.theme_use('clam')

style.configure("TLabelFrame", background="#B0E0E6", foreground="#000080", font=("Arial", 11, "bold"))
style.configure("TLabel", background="#F0F8FF", font=("Arial", 10))
style.configure("TButton", background="#4682B4", foreground="white", font=("Arial", 11, "bold"))
style.map("TButton",
          foreground=[('active', 'white')],
          background=[('active', '#5A9BD5')])

style.configure("TCombobox", fieldbackground="white", background="white", font=("Arial", 10))

# Título
titulo = tk.Label(ventana, text="Menú de Compra", font=("Arial", 18, "bold"), bg="#F0F8FF", fg="#000080")
titulo.pack(pady=15)

# ---------- Selección de tipo de carro ----------
frame_carro = ttk.LabelFrame(ventana, text="Tipo de carro")
frame_carro.pack(pady=8, fill="x", padx=20)

combo_carro = ttk.Combobox(frame_carro, values=["Automóvil", "Camioneta", "Camión"], textvariable=tipo_carro, state="readonly")
combo_carro.pack(padx=10, pady=5, fill="x")

# ---------- Selección de tipo de llanta ----------
frame_llanta = ttk.LabelFrame(ventana, text="Tipo de llanta")
frame_llanta.pack(pady=8, fill="x", padx=20)

combo_llanta = ttk.Combobox(frame_llanta, values=["Nieve", "Lluvia", "Carretera"], textvariable=tipo_llanta, state="readonly")
combo_llanta.pack(padx=10, pady=5, fill="x")

# ---------- Selección de marca ----------
frame_marca = ttk.LabelFrame(ventana, text="Marca")
frame_marca.pack(pady=8, fill="x", padx=20)

combo_marca = ttk.Combobox(frame_marca, values=["Michelin", "Goodyear", "Pirelli"], textvariable=marca, state="readonly")
combo_marca.pack(padx=10, pady=5, fill="x")

# ---------- Selección de modelo de llanta ----------
frame_modelo = ttk.LabelFrame(ventana, text="Modelo de llanta")
frame_modelo.pack(pady=8, fill="x", padx=20)

combo_modelo = ttk.Combobox(frame_modelo, values=["x12", "z80", "f09"], textvariable=modelo_llanta, state="readonly")
combo_modelo.pack(padx=10, pady=5, fill="x")

# ---------- Formulario para tamaño, anchura y alto ----------
frame_formulario = ttk.LabelFrame(ventana, text="Datos adicionales")
frame_formulario.pack(pady=8, fill="x", padx=20)

etiquetas = ["Tamaño", "Anchura", "Alto"]
for etiqueta in etiquetas:
    etiqueta_label = ttk.Label(frame_formulario, text=etiqueta)
    etiqueta_label.pack(anchor="w", padx=10)
    entrada = ttk.Entry(frame_formulario)
    entrada.pack(padx=10, pady=5, fill="x")
    campos[etiqueta] = entrada

# ---------- Botón para mostrar resumen ----------
btn_guardar = ttk.Button(ventana, text="Mostrar Resumen", command=mostrar_resumen)
btn_guardar.pack(pady=20)

# Ejecutar la app
ventana.mainloop()