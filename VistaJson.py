import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.geometry("600x400")
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=20, padx=20)
        self.opcion_var = tk.StringVar(value="")
        self.datos_texto = tk.Text(self.ventana, height=10, width=70)
        self.datos_texto.pack(pady=10)

    def mostrar_menu(self, callback):
        self.limpiar_contenedor()
        
        texto1 = tk.Label(self.contenedor, text="Por Favor Elige Una Opcion:")
        texto1.pack()

        opciones = ["1. Crear", "2. Leer", "3. Actualizar", "4. Eliminar", "5. Salir"]
        for opcion in opciones:
            tk.Label(self.contenedor, text=opcion).pack()

        opcion_entry = tk.Entry(self.contenedor, textvariable=self.opcion_var)
        opcion_entry.pack()
        
        def aceptar_callback():
            callback(self.opcion_var.get())
        
        boton_aceptar = tk.Button(self.contenedor, text="Aceptar", command=aceptar_callback)
        boton_aceptar.pack()
        
    def obtener_datos(self, callback_volver):
        self.limpiar_contenedor()
        
        nombre_var = tk.StringVar()
        nombre_label = tk.Label(self.contenedor, text="Nombre")
        nombre_label.pack()
        nombre_entry = tk.Entry(self.contenedor, textvariable=nombre_var)
        nombre_entry.pack()
        
        apellido_var = tk.StringVar()
        apellido_label = tk.Label(self.contenedor, text="Apellidos")
        apellido_label.pack()
        apellido_entry = tk.Entry(self.contenedor, textvariable=apellido_var)
        apellido_entry.pack()
        
        edad_var = tk.IntVar()
        edad_label = tk.Label(self.contenedor, text="Edad")
        edad_label.pack()
        edad_entry = tk.Entry(self.contenedor, textvariable=edad_var)
        edad_entry.pack()
        
        sexo_var = tk.StringVar()
        sexo_label = tk.Label(self.contenedor, text="Sexo")
        sexo_label.pack()
        sexo_entry = tk.Entry(self.contenedor, textvariable=sexo_var)
        sexo_entry.pack()
        
        def guardar_datos():
            datos = {
                'nombre': nombre_var.get(),
                'apellido': apellido_var.get(),
                'edad': edad_var.get(),
                'sexo': sexo_var.get()
            }
            callback_volver(datos)
        
        boton_registrar = tk.Button(self.contenedor, text="Registrar", command=guardar_datos)
        boton_registrar.pack()
        
        boton_atras = tk.Button(self.contenedor, text="Atras", command=lambda: callback_volver(None))
        boton_atras.pack()
        
        return {'nombre': nombre_var, 'apellido': apellido_var, 'edad': edad_var, 'sexo': sexo_var}

    def mostrar_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    def mostrar_exito(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_datos(self, datos):
        self.datos_texto.delete(1.0, tk.END)
        for index, item in enumerate(datos):
            self.datos_texto.insert(tk.END, f"{index}. {item}\n")

    def obtener_indice(self, callback, callback_volver):
        self.limpiar_contenedor()
        
        indice_label = tk.Label(self.contenedor, text="Posición")
        indice_label.pack()
        indice_var = tk.StringVar()
        indice_entry = tk.Entry(self.contenedor, textvariable=indice_var)
        indice_entry.pack()
        
        def aceptar_callback():
            callback(indice_var.get())
        
        boton_ok = tk.Button(self.contenedor, text="Ok", command=aceptar_callback)
        boton_ok.pack()
        
        boton_regresar = tk.Button(self.contenedor, text="Regresar", command=lambda: callback_volver())
        boton_regresar.pack()
        
        return indice_var

    def actualizar_datos(self, index, modelo, callback_volver):
        self.limpiar_contenedor()

        datos_actuales = modelo.leer()[index]

        nombre_var = tk.StringVar(value=datos_actuales['nombre'])
        nombre_label = tk.Label(self.contenedor, text="Nombre")
        nombre_label.pack()
        nombre_entry = tk.Entry(self.contenedor, textvariable=nombre_var, state=tk.NORMAL)
        nombre_entry.pack()
    
        apellido_var = tk.StringVar(value=datos_actuales['apellido'])
        apellido_label = tk.Label(self.contenedor, text="Apellidos")
        apellido_label.pack()
        apellido_entry = tk.Entry(self.contenedor, textvariable=apellido_var, state=tk.NORMAL)
        apellido_entry.pack()
    
        edad_var = tk.IntVar(value=datos_actuales['edad'])
        edad_label = tk.Label(self.contenedor, text="Edad")
        edad_label.pack()
        edad_entry = tk.Entry(self.contenedor, textvariable=edad_var, state=tk.NORMAL)
        edad_entry.pack()
    
        sexo_var = tk.StringVar(value=datos_actuales['sexo'])
        sexo_label = tk.Label(self.contenedor, text="Sexo")
        sexo_label.pack()
        sexo_entry = tk.Entry(self.contenedor, textvariable=sexo_var, state=tk.NORMAL)
        sexo_entry.pack()
    
        def guardar_cambios():
            datos = {
                'Nombre': nombre_var.get(),
                'Apellido': apellido_var.get(),
                'Edad': edad_var.get(),
                'Sexo': sexo_var.get()
            }
            modelo.actualizar(index, datos)
            self.mostrar_exito("Éxitoso", "Registro de datos actualizado exitosamente.")
            self.mostrar_datos(modelo.leer())
            self.limpiar_contenedor()  
            callback_volver()

        boton_actualizar = tk.Button(self.contenedor, text="Actualizar", command=guardar_cambios)
        boton_actualizar.pack()

        boton_regresar = tk.Button(self.contenedor, text="Regresar", command=callback_volver)
        boton_regresar.pack()

    def limpiar_contenedor(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()
