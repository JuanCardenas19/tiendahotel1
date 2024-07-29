import json

class _Modelo:
    def __init__(self, archivo):
        self._archivo = archivo
        self._datos = self._cargar_datos()

    def _cargar_datos(self):
        try:
            with open(self._archivo, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _guardar_datos(self):
        with open(self._archivo, 'w') as file:
            json.dump(self._datos, file, indent=4)
            

    def crear(self, item):
        self._datos.append(item)
        self._guardar_datos()

    def leer(self):
        return self._datos

    def actualizar(self, index, item):
        if 0 <= index < len(self._datos):
            self._datos[index] = item
            self._guardar_datos()

    def eliminar(self, index):
        if 0 <= index < len(self._datos):
            del self._datos[index]
            self._guardar_datos()

    def get_datos(self):
        return self._datos

    def set_datos(self, nuevos_datos):
        self._datos = nuevos_datos
        self._guardar_datos()