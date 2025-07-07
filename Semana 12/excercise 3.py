# Un uso de herencia multiple puede ser la combinacion de comportamientos de diferentes clases 
# en una sola, de esta forma la clase puede aquirir nuevos poderes, atributos y métodos que antes no tenía,
# esto podría implicar tambien la habilidad de comunicarse con otras clases a traves de las clases heredadas

#Ejemplo, esta clase ventana que hereda 2 comportamientos que están implementados en otras clases 

class Dibujable:
    def dibujar(self):
        print("Dibujando")

class Redimensionable:
    def redimensionar(self):
        print("Redimensionando")

class Ventana(Dibujable, Redimensionable):
    pass

ventana = Ventana()
ventana.dibujar()         # Salida: Dibujando
ventana.redimensionar()   # Salida: Redimensionando