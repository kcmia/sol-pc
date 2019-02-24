def fValue(str):
    try:
        return float(strBase)
    except:
        return None

def inputFloat(msg, error):
    str = input(msg)
    result = fValue()
    while result == None:
        print(error)
        str = input(msg)
        result = fValue()
    return result

base = inputFloat("Introduce base: ", "base debe ser numérica")
altura = inputFloat("Introduce altura:", "altura debe ser numérica")

print("Area del triángulo: {:.2f}".format(base * altura / 2))
