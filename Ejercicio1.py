#Crear una clase Vehiculo que tenga los siguientes atributos
#Color, Ruedas y Puertas

#Crearemos la clase Coche que heredara de vehiculo los atributos
#Velocidad y cilindrada

#Crear la clase Coche y mostrarla por pantalla

class Vehiculo:
    color = ''
    ruedas = None
    puertas = None
    
class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    
miCoche = Coche

miCoche.cilindrada = 1200
miCoche.velocidad = 160
miCoche.color = 'Azul'
miCoche.ruedas = 4
miCoche.puertas = 4

print('Hola')
print(miCoche.cilindrada)
print(miCoche.velocidad)    
print(miCoche.color)
print(miCoche.puertas)
print(miCoche.ruedas)
