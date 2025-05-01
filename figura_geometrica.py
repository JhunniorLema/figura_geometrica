
class FiguraGeometrica:
    def __init__(self, color: str = "Sin color"):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        if isinstance(nuevo_color, str) and nuevo_color:
            self._color = nuevo_color
        else:
            raise ValueError("El color debe ser una cadena no vacía.")

    def area(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

    def perimetro(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

    def __str__(self):
        return f"Color: {self.color}"


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float, color: str = "Sin color"):
        super().__init__(color)
        self.lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._lado = valor
        else:
            raise ValueError("El lado debe ser un número positivo.")

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return f"Cuadrado de lado {self.lado}, área: {self.area()}, perímetro: {self.perimetro()}, color: {self.color}"


class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float, color: str = "Sin color"):
        super().__init__(color)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._base = valor
        else:
            raise ValueError("La base debe ser un número positivo.")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._altura = valor
        else:
            raise ValueError("La altura debe ser un número positivo.")

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo de base {self.base}, altura {self.altura}, área: {self.area()}, perímetro: {self.perimetro()}, color: {self.color}"


# Ejemplo de uso
cuadro = Cuadrado(5, "Azul")
print(cuadro)

rectangulo = Rectangulo(4, 6, "Rojo")
print(rectangulo)

# Modificar atributos
cuadro.lado = 10
rectangulo.altura = 8
print(cuadro)
print(rectangulo)
