
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


# Ejemplo de uso
cuadrado = Cuadrado(6)
print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())
