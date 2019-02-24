def fValue(x):
    try:
        return float(x)
    except:
        return None

def iValue(x):
    try:
        resultado = int(x)
        if resultado < 0:
            return None
        return resultado
    except:
        return None

def inputPrecio():
    msg = "introduce precio: "
    result = fValue(input(msg))
    while result == None:
        print("precio debe ser numérico")
        result = fValue(input(msg))
    return result

def inputUnidades():
    msg = "introduce unidades: "
    result = iValue(input(msg))
    while result == None:
        print("unidades debe ser entero positivo")
        result = iValue(input(msg))
    return result
