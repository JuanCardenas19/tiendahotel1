from ModeloJson import _Modelo
from VistaJson import Vista
from ControladorJson import Controlador

if __name__ == "__main__":
    modelo = _Modelo('info_privada.json')
    vista = Vista()
    controlador = Controlador(modelo, vista)
    controlador.ejecutar() 