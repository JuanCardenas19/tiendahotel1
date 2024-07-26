class transporte:  
  #************* ATRIBUTOS CLASE TRANSPORTE *************  
  def __init__(self,gasolinaVehiculo):
    
    self.tipo_Transporte = ''
    self.capacidad_Carga = 0
    self.tipo_Combustible = ''
    self.capacidad_Pasajeros = 0
    self.modelo=''
    self.marca=''
    self.gasolina=gasolinaVehiculo()   
    
  #************* MÉTODOS CLASE TRANSPORTE *************  
  
  def ingresar_Datos(self):
    self.tipo_Transporte = input('Ingrese el tipo de transporte: \n')
    self.capacidad_Carga = int('input("Ingrese la capacidad de carga: \n')
    self.tipo_Combustible = input('Ingrese el tipo de combustible: \n')
    self.capacidad_Pasajeros = int(input('Ingrese la capacidad de pasajeros: \n'))
    self.modelo = input('Ingrese el modelo: \n')
    self.marca = input('Ingrese la marca: \n')  
    
  def moverse(self):
    print('El transporte se está moviendo')   
    
  def frenar(self):
    print('El transporte se está frenando')
    
  def acelerar(self):      
    print('El transporte se está acelerando')
    
  def subir_pasajero(self):
    print('El transporte se está subiendo pasajeros')
    
  def bajar_pasajero(self):
    print('El transporte se está bajando pasajeros')
    
  def mostrar_datos(self):
    print('Tipo de transporte: ', self.tipo_Transporte)
    print('Capacidad de carga: ', self.capacidad_Carga)
    print('Tipo de combustible: ', self.tipo_Combustible)
    print('Capacidad de pasajeros: ', self.capacidad_Pasajeros)
    print('Modelo: ', self.modelo)
    print('Marca: ', self.marca)

class Transporte_Particular(transporte):
  def __init__(self):
    super().__init__(gasolinaVehiculo)

class Transporte_Publico(transporte ):
  def __init__(self):
    super().__init__(gasolinaVehiculo)
    
class gasolinaVehiculo: 
  def __init__(self):
    self.gasolina = ''
    def ingresar_gasolina(self):
      self.gasolina=input('Ingresar gasolina: \n')

gasolina=gasolinaVehiculo()
vehiculo=transporte(gasolina)
aux=vehiculo.ingresar_Datos()
print(aux)
