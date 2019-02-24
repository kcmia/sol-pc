from mis_inputs import *

lineas_factura = []
total = 0
totUnidades = 0

precio = inputPrecio()
unidades = inputUnidades()

while precio != 0 and unidades != 0:
    totUnidades += unidades
    subtotal = unidades * precio
    total += subtotal
    linea = '{:.2f}€ - {:d} - {:.2f}€'.format(precio, unidades, subtotal)
    lineas_factura.append(linea)

    precio = inputPrecio()
    unidades = inputUnidades() 

print()
print("FACTURA")

for linea in lineas_factura:
    print(linea)
print("------------------------")
print("Total: {:.2f}€".format(total))
print("Unidades: {}".format(totUnidades))
