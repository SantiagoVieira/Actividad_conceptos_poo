import math
if __name__ == "__main__":
    class Punto:
        def __init__(self,x:int,y:int):
            self.x:int = x
            self.y:int = y

        def mostrar_coordenadas(self):
            return print(f"{self.x},{self.y}")

        def Mover_punto(self,dx:int,dy:int):
            self.x:int = self.x + dx
            self.y: int = self.y + dy

        def distacia_punto(self,punto_diferente):
            termino_1 = punto_diferente.x - self.x
            termino_2 = punto_diferente.y - self.y
            calculo = math.sqrt(termino_1 ** 2) + (termino_2 ** 2)
            return calculo




    punto_1 = Punto(5,5)
    punto_2 = Punto(5,5)
    punto_1.mostrar_coordenadas()
    punto_1.Mover_punto(-5,4)
    punto_1.mostrar_coordenadas()

    punto_1.distacia_punto(punto_2)
