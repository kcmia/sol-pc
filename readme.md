# Soluciones a la practica del módulo Pensamiento Computacional
## Área de un triángulo
Empezamos con un esquema general como el que figura en `triangulo/posible_evolucion/version1.py`. 
Validamos cada input con un esquema clásico de try-except y provocamos la salida en caso de error con `quit()`.
Como esta solución es un poco drástica buscando en la documentación encontramos una forma de provocar la finalización de nuestro script sin que se produzca error con `os._exit(0)` como se ve en `triangulo/posible_evolucion/version1.01.py`
El siguiente paso es que en lugar de acabar el programa montemos un bucle de petición del dato cada vez que sea erróneo. En formato más básico se ve en `triangulo/posible_evolucion/version2.py`.
Revisando el código queda claro que repetimos mucho la petición `strBase = input...` y el ciclo try-except de validación (lineas 3 a 6 y 13 a 16). Esto pide a gritos una refactorización utilizando funciones. Aunque es el primer módulo sabemos hacerlo.
Nota: Es importante hacer notar que en este programa se usa un patrón de diseño muy común con los bucles while:
```
Primera lectura o input
Primera validación
+- While condición tras lectura
|   <Procesar datos>
|   lectura o input
|    validación
+-
```
Nos aseguramos así de a) siempre leer al menos una vez y b) procesar la última entrada. Es un patrón que usaremos muy a menudo.
### Primera refactorización
1. Sacamos la validación a una función `fValue` lo que ya deja el código más legible `triangulo/posible_evolución/version2.01.py`.
2. Sacamos también el ciclo de petición hasta que esté correcto a otra función `inputFloat`. Ahora nuestro código se queda reducido de nuevo a nuestra idea inicial:
    - Input Base
    - Inptu Altura
    - Imprimir Area = Base * Altura / 2
    Se ve con claridad en `triangulo/posible_evolucion/version2.02.py``

### Versión final
Como las funciones iniciales fastidian la legilibilidad del programa creamos un módulo llamado `mis_inputs.py`. La ventaja además será que podremos reutilizar este módulo o una copia en el siguiente ejercicio.

Esto se ve en `triangulo/posible_evolución/version3.py`



1. - quitar quit -> stack overflow nos lleva a <versión1.01.py>
2. - que vuelva a pedir el valor <version2.py> -> transformar el if -> exit en un bucle while. Hacer notar la estructura.
	- 1ª ejecución fuera incluyendo transformación
	- while comprobación
	- mensaj de error
	- repetición del input
Huele un poco... muchas repeticiones. Entran las funciones.
3. - Limpieza -> <version2.1.py> -> 
	1.- primera iteración quitar los try-exept repetidos (son muchos) -> fValue
	2.- segunda iteración quitar la estructura while 

Esta versión ya es una buena solución. Pero podemos generalizarla y modularizarla sacando la función de entrada a un módulo para reutilizarla -> <main.py + mis_inputs.py>
