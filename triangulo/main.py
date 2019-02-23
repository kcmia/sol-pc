def area(b, h):
    return b * h / 2

def fValue(x):
    try:
        return float(x)
    except:
        return None
   
def inputFloat(msg, error):
    result = fValue(input(msg))
    while result == None:
        print(error)
        result = fValue(input(msg))
    return result

base = inputFloat("Introduce base: ", "base debe ser numérico")
altura = inputFloat("Introduce altura: ", "altura debe ser numérico")

print("Area del triángulo: {:.2f}".format(area(base, altura)))    
