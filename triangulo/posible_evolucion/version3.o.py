from mis_inputs import inputFloat, fValue
from triangulo import Triangulo
import sys

if __name__ == "__main__":
    base = None
    altura = None
    if len(sys.argv) >= 2:
        base = fValue(sys.argv[1])
        if len(sys.argv) > 2:
            altura = fValue(sys.argv[2])

    if base == None:
        base = inputFloat("Introduce base: ", "base debe ser numérica")
    if altura == None:
        altura = inputFloat("Introduce altura: ", "altura debe ser numérica")
            
    t = Triangulo(base, altura)

    print("Area del triángulo: {:.2f}".format(t.area()))
