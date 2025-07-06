import tkinter as tk
from tkinter import messagebox

# Lista de marcas y modelos iniciales
marcas_llantas = ["Michelin", "Goodyear", "Pirelli"]
modelos_llantas = ["X12", "Z80", "F79"]
tipos_llantas = ["Carretera", "Todo Terreno"]
inventario = {}  # clave: (marca, modelo, tipo, medida, estado) -> valor: cantidad

def actualizar_menus():
    """Actualiza todos los menús desplegables con las nuevas opciones"""
    # Actualizar menú principal
    menu_marca['menu'].delete(0, 'end')
    for marca in marcas_llantas:
        menu_marca['menu'].add_command(label=marca, command=tk._setit(marca_var, marca))
    
    menu_modelo['menu'].delete(0, 'end')
    for modelo in modelos_llantas:
        menu_modelo['menu'].add_command(label=modelo, command=tk._setit(modelos_var, modelo))
    
    menu_tipo['menu'].delete(0, 'end')
    for tipo in tipos_llantas:
        menu_tipo['menu'].add_command(label=tipo, command=tk._setit(tipo_var, tipo))

# Función para actualizar inventario desde ventana principal
def actualizar_inventario(es_entrada=True):
    marca = marca_var.get()
    modelo = modelos_var.get()
    tipo = tipo_var.get()
    medida_ancho = entry_ancho.get().strip()
    medida_alto = entry_alto.get().strip()
    estado = estado_var.get()
    cantidad_str = entry_cantidad.get().strip()
    ubicacion = ubicacion_var.get()

    if not all([marca, modelo, medida_ancho, medida_alto, cantidad_str]):
        messagebox.showwarning("Datos incompletos", "Por favor llena todos los campos.")
        return

    if not medida_ancho.isdigit() or not medida_alto.isdigit() or not cantidad_str.isdigit():
        messagebox.showerror("Error de formato", "Las medidas y cantidad deben ser números.")
        return

    cantidad = int(cantidad_str)
    clave = (marca, modelo, tipo, f"{medida_ancho}/{medida_alto}", estado)

    if es_entrada:
        inventario[clave] = inventario.get(clave, 0) + cantidad
        accion = "Entrada registrada"
        signo = "+"
    else:
        if clave not in inventario or inventario[clave] < cantidad:
            messagebox.showerror("Inventario insuficiente", "No hay suficiente producto para esta salida.")
            return
        inventario[clave] -= cantidad
        accion = "Salida registrada"
        signo = "-"

    mensaje = (
        f"{accion}:\n"
        f"Marca: {marca}, Modelo: {modelo}\n"
        f"Tipo: {tipo}, Estado: {estado}\n"
        f"Medida: {medida_ancho}/{medida_alto}, Cantidad: {signo}{cantidad}\n"
        f"Ubicación: {ubicacion}\n"
        f"Cantidad total actual: {inventario[clave]}"
    )
    messagebox.showinfo("Actualización de Inventario", mensaje)
    
    # Limpiar campos después de registrar
    entry_ancho.delete(0, tk.END)
    entry_alto.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

# Función para abrir ventana de agregar nuevas opciones al catálogo
def abrir_ventana_agregar_catalogo():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Agregar")
    nueva_ventana.geometry("400x300")
    nueva_ventana.configure(bg="#f0f2f5")

    tk.Label(
        nueva_ventana,
        text="Agregar Nuevas Opciones",
        font=("Segoe UI", 14, "bold"),
        bg="#d0f0fd",
        fg="#0d6efd"
    ).pack(pady=10, fill="x")

    frame_catalogo = tk.Frame(nueva_ventana, bg="white", bd=2, relief="groove", padx=20, pady=20)
    frame_catalogo.pack(padx=20, pady=10, fill="both", expand=True)

    # Entradas para nuevos valores
    tk.Label(frame_catalogo, text="Nueva Marca:", bg="white", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="e", pady=10, padx=10)
    entry_nueva_marca = tk.Entry(frame_catalogo, width=25, font=("Segoe UI", 10))
    entry_nueva_marca.grid(row=0, column=1, sticky="w", pady=10)

    tk.Label(frame_catalogo, text="Nuevo Modelo:", bg="white", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", pady=10, padx=10)
    entry_nuevo_modelo = tk.Entry(frame_catalogo, width=25, font=("Segoe UI", 10))
    entry_nuevo_modelo.grid(row=1, column=1, sticky="w", pady=10)

    tk.Label(frame_catalogo, text="Nuevo Tipo:", bg="white", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="e", pady=10, padx=10)
    entry_nuevo_tipo = tk.Entry(frame_catalogo, width=25, font=("Segoe UI", 10))
    entry_nuevo_tipo.grid(row=2, column=1, sticky="w", pady=10)

    def agregar_al_catalogo():
        nueva_marca = entry_nueva_marca.get().strip()
        nuevo_modelo = entry_nuevo_modelo.get().strip()
        nuevo_tipo = entry_nuevo_tipo.get().strip()
        
        agregados = []

        if nueva_marca and nueva_marca not in marcas_llantas:
            marcas_llantas.append(nueva_marca)
            agregados.append(f"Marca: {nueva_marca}")

        if nuevo_modelo and nuevo_modelo not in modelos_llantas:
            modelos_llantas.append(nuevo_modelo)
            agregados.append(f"Modelo: {nuevo_modelo}")

        if nuevo_tipo and nuevo_tipo not in tipos_llantas:
            tipos_llantas.append(nuevo_tipo)
            agregados.append(f"Tipo: {nuevo_tipo}")

        if agregados:
            actualizar_menus()
            mensaje = "Se agregaron al catálogo:\n" + "\n".join(agregados)
            messagebox.showinfo("Catálogo actualizado", mensaje)
            nueva_ventana.destroy()
        else:
            messagebox.showwarning("Sin cambios", "No se agregaron nuevos elementos o ya existían.")

    tk.Button(
        frame_catalogo, 
        text="Agregar", 
        command=agregar_al_catalogo, 
        bg="#0d6efd", 
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=20
    ).grid(row=3, column=0, columnspan=2, pady=20)

# Función para ver el inventario actual
def ver_inventario():
    ventana_inventario = tk.Toplevel(ventana)
    ventana_inventario.title("Inventario Actual")
    ventana_inventario.geometry("800x600")
    ventana_inventario.configure(bg="#f0f2f5")

    tk.Label(
        ventana_inventario,
        text="Inventario Actual",
        font=("Segoe UI", 16, "bold"),
        bg="#d0f0fd",
        fg="#0d6efd"
    ).pack(pady=10, fill="x")

    frame_inventario = tk.Frame(ventana_inventario, bg="white")
    frame_inventario.pack(padx=20, pady=10, fill="both", expand=True)

    # Crear scrollbar
    scrollbar = tk.Scrollbar(frame_inventario)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Crear texto con scrollbar
    texto_inventario = tk.Text(frame_inventario, yscrollcommand=scrollbar.set, font=("Consolas", 10))
    texto_inventario.pack(side=tk.LEFT, fill="both", expand=True)
    scrollbar.config(command=texto_inventario.yview)

    if not inventario:
        texto_inventario.insert(tk.END, "El inventario está vacío.")
    else:
        texto_inventario.insert(tk.END, "INVENTARIO ACTUAL\n")
        texto_inventario.insert(tk.END, "="*60 + "\n\n")
        
        for clave, cantidad in inventario.items():
            if cantidad > 0:  # Solo mostrar productos con cantidad > 0
                marca, modelo, tipo, medida, estado = clave
                texto_inventario.insert(tk.END, f"Marca: {marca}\n")
                texto_inventario.insert(tk.END, f"Modelo: {modelo}\n")
                texto_inventario.insert(tk.END, f"Tipo: {tipo}\n")
                texto_inventario.insert(tk.END, f"Medida: {medida}\n")
                texto_inventario.insert(tk.END, f"Estado: {estado}\n")
                texto_inventario.insert(tk.END, f"Cantidad: {cantidad}\n")
                texto_inventario.insert(tk.END, "-"*40 + "\n\n")

    texto_inventario.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de producto - Almacén")
ventana.geometry("650x700")
ventana.configure(bg="#f0f2f5")

tk.Label(
    ventana,
    text="Registro de producto - Almacén",
    font=("Segoe UI", 18, "bold"),
    bg="#d0f0fd",
    fg="#0d6efd"
).pack(pady=20, fill="x")

# Frame principal para registro
frame = tk.Frame(ventana, bg="white", bd=2, relief="groove", padx=20, pady=20)
frame.pack(padx=20, pady=10)

etiqueta_config = {"bg": "white", "font": ("Segoe UI", 10)}
entrada_config = {"width": 30, "font": ("Segoe UI", 10)}

def crear_fila(texto, fila, widget):
    tk.Label(frame, text=texto, **etiqueta_config).grid(row=fila, column=0, sticky="e", pady=5, padx=10)
    widget.grid(row=fila, column=1, sticky="w", pady=5)

marca_var = tk.StringVar(value=marcas_llantas[0])
menu_marca = tk.OptionMenu(frame, marca_var, *marcas_llantas)
menu_marca.config(width=28, font=("Segoe UI", 9))
crear_fila("Marca de llanta:", 0, menu_marca)

modelos_var = tk.StringVar(value=modelos_llantas[0])
menu_modelo = tk.OptionMenu(frame, modelos_var, *modelos_llantas)
menu_modelo.config(width=28, font=("Segoe UI", 9))
crear_fila("Modelo de llanta:", 1, menu_modelo)

tipo_var = tk.StringVar(value=tipos_llantas[0])
menu_tipo = tk.OptionMenu(frame, tipo_var, *tipos_llantas)
menu_tipo.config(width=28, font=("Segoe UI", 9))
crear_fila("Tipo:", 2, menu_tipo)

entry_ancho = tk.Entry(frame, width=10, font=("Segoe UI", 10))
crear_fila("Medida - Ancho:", 3, entry_ancho)

entry_alto = tk.Entry(frame, width=10, font=("Segoe UI", 10))
crear_fila("Medida - Alto:", 4, entry_alto)

estado_var = tk.StringVar(value="Nueva")
menu_estado = tk.OptionMenu(frame, estado_var, "Nueva", "Seminueva")
menu_estado.config(width=28, font=("Segoe UI", 9))
crear_fila("Estado del producto:", 5, menu_estado)

entry_cantidad = tk.Entry(frame, width=10, font=("Segoe UI", 10))
crear_fila("Cantidad:", 6, entry_cantidad)

ubicacion_var = tk.StringVar(value="Por tipo")
menu_ubicacion = tk.OptionMenu(frame, ubicacion_var, "Por tipo", "Por medida", "Por estado")
menu_ubicacion.config(width=28, font=("Segoe UI", 9))
crear_fila("Ubicación en almacén:", 7, menu_ubicacion)

# Frame para botones de gestión
frame_botones_gestion = tk.Frame(ventana, bg="#f0f2f5")
frame_botones_gestion.pack(pady=10)

tk.Button(
    frame_botones_gestion,
    text="Agregar",
    command=abrir_ventana_agregar_catalogo,
    bg="#6f42c1",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20
).pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_botones_gestion,
    text="Ver Inventario",
    command=ver_inventario,
    bg="#17a2b8",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20
).pack(side=tk.LEFT, padx=5)

# Frame para botones de inventario
frame_botones_inventario = tk.Frame(ventana, bg="#f0f2f5")
frame_botones_inventario.pack(pady=10)

tk.Button(
    frame_botones_inventario,
    text="Registrar Entrada de Producto",
    command=lambda: actualizar_inventario(es_entrada=True),
    bg="#198754",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=30
).pack(pady=5)

tk.Button(
    frame_botones_inventario,
    text="Registrar Salida de Producto",
    command=lambda: actualizar_inventario(es_entrada=False),
    bg="#ffc107",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    width=30
).pack(pady=5)

tk.Button(
    ventana,
    text="Salir",
    command=ventana.quit,
    bg="#dc3545",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=30
).pack(pady=20)

ventana.mainloop()