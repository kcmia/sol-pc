def fValue(str):
    try:
        return float(strBase)
    except:
        return None



strBase = input("Introduce base: ")
base = fValue(strBase)

while base == None:
    print("base debe ser numérica")

    strBase = input("Introduce base: ")
    base = fValue(strBase)

strAltura = input("Introduce altura: ")
altura = fValue(strAltura)

while altura == None:
    print("base debe ser numérica")

    strAltura = input("Introduce altura: ")
    altura = fValue 
           
print("Area del triángulo: {:.2f}".format(base * altura / 2))
