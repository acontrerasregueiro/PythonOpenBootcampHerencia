#En este segundo ejercicio, tendreis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. 
# Debereis de definir los metodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = ''
    nota = None
    
    def __init__(self,nombre, nota):
        print('El nombre del alumno es : ', nombre)
        print('La nota del alumno es : ', nota)
           
persona = Alumno("Javier Perez Perez", 7.8)


        