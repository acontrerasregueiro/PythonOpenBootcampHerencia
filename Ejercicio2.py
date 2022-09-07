#En este segundo ejercicio, tendreis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. 
# Debereis de definir los metodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = ''
    nota = 0    
    
    def ponerNota(self):
        self.nota = 6.6       
    
    def ponerNombre(self):
        self.nombre = "Perico de los palotes"
        
    def isAprobado(self):
        print(self.nota)
        if (self.nota > 5):
            return("Aprobado")
        else:
            return("Suspenso")         

persona2 = Alumno
persona2.ponerNombre(persona2)
persona2.ponerNota(persona2)

print('La nota de ' ,persona2.nombre, 'Es : ',persona2.nota)
print(persona2.isAprobado(persona2))


        