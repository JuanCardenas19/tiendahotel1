class Controlador:
    def __init__(self, modelo, vista):
        self._modelo = modelo
        self._vista = vista

    def ejecutar(self):
        self._vista.mostrar_menu(self.procesar_opcion)
        self._vista.ventana.mainloop()

    def procesar_opcion(self, opcion_str):
        try:
            opcion = int(opcion_str)
        except ValueError:
            self._vista.mostrar_error("Error", "Opción Incorrecta.")
            self._vista.mostrar_menu(self.procesar_opcion)
            return

        if opcion == 1:
            self.crear()
        elif opcion == 2:
            self.leer()
        elif opcion == 3:
            self.actualizar()
        elif opcion == 4:
            self.eliminar()
        elif opcion == 5:
            self._vista.ventana.quit()
        else:
            self._vista.mostrar_error("Error", "Opción Incorrecta.")
            self._vista.mostrar_menu(self.procesar_opcion)

    def crear(self):
        def volver(datos):
            if datos:
                self._modelo.crear(datos)
                self._vista.mostrar_exito("Éxitoso", "El Registro A Sido Creado Exitosamente.")
                self._vista.mostrar_datos(self._modelo.leer())
            self._vista.mostrar_menu(self.procesar_opcion)

        self._vista.obtener_datos(volver)

    def leer(self):
        datos = self._modelo.leer()
        self._vista.mostrar_datos(datos)
        self._vista.mostrar_menu(self.procesar_opcion)

    def actualizar(self):
        def volver():
            self._vista.mostrar_menu(self.procesar_opcion)

        self._vista.obtener_indice(lambda indice_str: self.procesar_actualizar(indice_str, volver), volver)

    def procesar_actualizar(self, indice_str, callback_volver):
        try:
            index = int(indice_str)
        except ValueError:
            self._vista.mostrar_error("Error", "Posicion Incorrecta.")
            self._vista.mostrar_menu(self.procesar_opcion)
            return

        self._vista.actualizar_datos(index, self._modelo, callback_volver)


    def eliminar(self):
        def volver():
            self._vista.mostrar_menu(self.procesar_opcion)

        self._vista.obtener_indice(lambda indice_str: self.procesar_eliminar(indice_str, volver), volver)

    def procesar_eliminar(self, indice_str, callback_volver):
        try:
            index = int(indice_str)
        except ValueError:
            self._vista.mostrar_error("Error", "Posicion Incorrecta.")
            self._vista.mostrar_menu(self.procesar_opcion)
            return

        self._modelo.eliminar(index)
        self._vista.mostrar_exito("Éxito", "El Registro A Sido Eliminado Exitosamente.")
        self._vista.mostrar_datos(self._modelo.leer())
        callback_volver()
