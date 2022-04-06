import math

print("A continuación vamos a ir desarrollando las consignas del Homework")
print("_Consigna 1: Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla")
a = 2
print(a)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 2: Imprimir el tipo de dato de la constante 8.5")
x = 8.5
print(type(x))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consgina 3: Imprimir el tipo de dato de la variable creada en el punto 1")
print(type(a))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consgina 4: Crear una variable que contenga tu nombre")
miNombre = "Juan Manuel Facundo Amarilla"
print("Mi nombre es: ", miNombre)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consgina 5: Crear una variable que contenga un número complejo")
numeroComplejo = 666 + 1j
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consgina 5: Mostrar el tipo de dato de la variable crada en el punto 5")
print(type(numeroComplejo))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 7: Crear una variable que contenga el valor del número Pi redondeado a 4 decimales")
numeroPi = round(3.141592, 4)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 8: Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?")
x = True
y = True
z = x == y
zz = x != y
a = 2 + 2
b = 4
c = a == b
cc = b != a
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 9: Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9")
print(z, zz, c, cc)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 10: Asignar a una variable, la suma de un número entero y otro decimal")
numeroEntero = 2
numeroDecimal = 2.5
t = numeroEntero + numeroDecimal
h = t
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 11: Realizar una operación de suma de números complejos")
numI1 = 5j
numI2 = 3J
print(5j + 3J)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 12: Realizar una operación de suma de un número real y otro complejo")
numReal = 4813
numComplejo = 1j
print(numReal + numComplejo)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 13: Realizar una operación de multiplicación")
op = 2 * 2
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 14: Mostrar el resultado de elevar 2 a la octava potencia")
print(2**8)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 15: Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla")
coc = 27/4
print(coc)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 16: De la división anterior solamente mostrar la parte entera")
print(math.trunc(coc))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 17: De la división de 27 entre 4 mostrar solamente el resto")
print(24 % 7)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 18: Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado")
print((4 * (math.trunc(coc))) + (24 % 7))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 19: Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas")
print("Trinity54" + "36Rabbit")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 20: Evaluar si '2' es igual a 2. ¿Por qué ocurre eso?")
gon = "2"
ant = 2
print(gon == ant) #Problema de sintaxis -No usar doble comilla dentro de doble comilla.
# Además NO se puede sumar variables con != tipo de datos. Sin embargo, SÍ puede hacerse si se Re-convierten
# las variables.
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 21: Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera")
print(str(gon) == str(ant))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 22: ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')")
print("Porque NO puede convertirse una cadena a punto flotante")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 23: Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido")
la = 3
la -= 1
print(la)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 24: Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?")
num555 = 1 << 2
print(num555)
print("Creo que desplaza los valores en bit hacia la izquierda y luego los sumas")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 25: Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?")
print("NO entendí la consigna :(")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print("_Consigna 26: Realizar una operación válida entre valores de tipo entero y string")
numEntero = 2
varEstring = '2'
print(numEntero + int(varEstring))
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

