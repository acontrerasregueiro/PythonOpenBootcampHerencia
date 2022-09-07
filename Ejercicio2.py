#En este segundo ejercicio, tendreis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. 
# Debereis de definir los metodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = ''
    nota = None
    
    
    #Ejemplo con constructor
    def __init__(self,nombre, nota):
        print('El nombre del alumno es : ', nombre)
        print('La nota del alumno es : ', nota)
        
    #Ejemplo con metodos    
    def ponerNota(self,puntuacion):
        nota = 6.6
    
    def ponerNombre(self,name):
        nombre = name
           
persona = Alumno("Javier Perez Perez", 7.8)

persona2 = Alumno
persona2.nombre = "Pedro Lopez Lopez"
persona2.nota = 6.6

print('La nota de ' ,persona2.nombre, 'Es : ',persona2.nota)


        