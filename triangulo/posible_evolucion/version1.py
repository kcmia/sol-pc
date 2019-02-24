strBase = input("Introduce base: ")

try:
    base = float(strBase)
except:
    base = None

if base == None:
    print("base debe ser numérica")
    quit()

strAltura = input("Introduce altura: ")

try:
    altura = float(strBase)
except:
    altura = None

if altura == None:
    print("base debe ser numérica")
    quit()

print("Area del triángulo: {:.2f}".format(base * altura / 2))
