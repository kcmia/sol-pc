class Triangulo():
    def __init__(self, base=1, altura=1):
        self.base = base
        self.altura = altura

    def __str__():
        return 'Triangulo(b: {}, h: {})'.format(self.base, self.altura)

    def area(self):
        return self.base * self.altura / 2

