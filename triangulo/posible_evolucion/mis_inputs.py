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
