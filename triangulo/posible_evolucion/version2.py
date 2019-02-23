strBase = input("Introduce base: ")

try:
    base = float(strBase)
except:
    base = None

while base == None:
    print("base debe ser numérica")

    strBase = input("Introduce base: ")

    try:
        base = float(strBase)
    except:
        base = None

strAltura = input("Introduce altura: ")

try:
    altura = float(strBase)
except:
    altura = None

while altura == None:
    print("base debe ser numérica")

    strAltura = input("Introduce altura: ")

    try:
        altura = float(strBase)
    except:
        altura = None
        
print("Area del triángulo: {:.2f}".format(base * altura / 2))
