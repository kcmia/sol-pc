from mis_inputs import inputFloat

def area(b, h):
    return b * h / 2
   
base = inputFloat("Introduce base: ", "base debe ser numérico")
altura = inputFloat("Introduce altura: ", "altura debe ser numérico")

print("Area del triángulo: {:.2f}".format(area(base, altura)))    
