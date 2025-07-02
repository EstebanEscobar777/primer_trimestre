# # persona={

# # "nombre":"Juan",
# # "edad": 30,
# # "Lugnacimiento":"Palmira"

# # }

# auto={

# "marca":"ford",
# "modelo":"Mustang",
# "año":2022,
# "color":"azul",
# "placa":"LSD-344"

# }

# auto["año"]=2023

# print(auto["año"])

# # --------eliminacion-------


# del auto["modelo"]
# auto.pop("marca")

# -----------ejercicio_practico---------------

# n1=float(input("ingrese la primera nota: "))
# n2=float(input("ingrese la segunda nota: "))
# n3=float(input("ingrese la tercera nota: "))
# lista=[]
# lista.append(n1)
# lista.append(n2)
# lista.append(n3)
# suma=n1+n2+n3
# ope=suma/3
# print(lista)
# print(f"el promedio de sus notas es: {ope}")

# # ----------------------ejercicio2----------------

# productos={

# "pan":1000,
# "leche":2500,
# "huevos":3000

# }
# print(productos)

# porc=float(input("ingrese el porcentaje que desea aumentar: "))
# productos["pan"]+= productos["pan"]*(porc/100)
# productos["leche"]+= productos["leche"]*(porc/100)
# productos["huevos"]+= productos["huevos"]*(porc/100)

# print(productos)

# ------------------------------ejercicio3-----------------------------

# temperatura=[]

# temp=float (input("ingrese la primer temperatura: "))
# temp2=float (input("ingrese la segunda temperatura: "))
# temp3=float (input("ingrese la tercera temperatura: "))
# temp4=float (input("ingrese la cuarta temperatura: "))
# temp5=float (input("ingrese la quinta temperatura: "))

# celsius=(temp, temp2, temp3, temp4, temp5)

# ope=temp*9/5+32
# ope2=temp2*9/5+32
# ope3=temp2*9/5+32
# ope4=temp2*9/5+32
# ope5=temp2*9/5+32

# fahrenheit=(ope, ope2, ope3, ope4, ope5)

# print(f"temperaturas en °C",celsius)
# print("temperatura en °F:", fahrenheit)

# -----------------ejercicio4----------------

# edades=[int(input("edad 1: ")),int(input("edad 2: ")),int(input("edad 3: ")),int(input("edad 4: ")),int(input("edad 5: "))]
# promedio=sum(edades)/len(edades)
# print(f"Mayor: {max(edades)}, Menor: {min(edades)}, promedio: {promedio}")

# --------------ejercicio5------------

# frutas={

# "uva": "precio por kilo 2000",
# "pera":"precio por kilo 3000",
# "sandia": "precio por kilo 5000"


# }

# print(frutas)

# kil=int(input("ingrese la cantiada de kilos que desea de la uva: "))
# kil1=int(input("ingrese la cantiada de kilos que desea de la pera: "))
# kil2=int(input("ingrese la cantiada de kilos que desea de la sandia: "))

# ope=kil*2000
# ope1=kil1*3000
# ope2=kil2*5000

# suma=ope+ope1+ope2

# print(f"el total a pagar es: {suma}")

# -----------------ejercicio6------------------

# a=int(input("ingrese el primer numero: "))
# b=int(input("ingrese el primer numero: "))
# c=int(input("ingrese el primer numero: "))
# d=int(input("ingrese el primer numero: "))
# e=int(input("ingrese el primer numero: "))

# tupla=(a, b, c, d, e)

# print("la suma total es:", sum(tupla))

# --------------------ejercicio7----------------

# inventario = []

# nombre1 = input("Nombre del producto 1: ")
# cantidad1 = int(input("Cantidad del producto 1: "))
# precio1 = float(input("Precio del producto 1: "))
# producto1 = {"nombre": nombre1, "cantidad": cantidad1, "precio": precio1}
# inventario.append(producto1)

# nombre2 = input("Nombre del producto 2: ")
# cantidad2 = int(input("Cantidad del producto 2: "))
# precio2 = float(input("Precio del producto 2: "))
# producto2 = {"nombre": nombre2, "cantidad": cantidad2, "precio": precio2}
# inventario.append(producto2)

# nombre3 = input("Nombre del producto 3: ")
# cantidad3 = int(input("Cantidad del producto 3: "))
# precio3 = float(input("Precio del producto 3: "))
# producto3 = {"nombre": nombre3, "cantidad": cantidad3, "precio": precio3}
# inventario.append(producto3)

# total = (
#     producto1["cantidad"] * producto1["precio"] +
#     producto2["cantidad"] * producto2["precio"] +
#     producto3["cantidad"] * producto3["precio"]
# )


# print("\nEl valor total del inventario es:", total)

# --------------------ejercicio8-------------------

# precios = [100, 200, 300, 400, 500]

# descuento = float(input("Ingresa el descuento en porcentaje: "))
# descuento = descuento / 100

# precios[0] = precios[0] - precios[0] * descuento
# precios[1] = precios[1] - precios[1] * descuento
# precios[2] = precios[2] - precios[2] * descuento
# precios[3] = precios[3] - precios[3] * descuento
# precios[4] = precios[4] - precios[4] * descuento

# print("Precios con descuento:", precios)

# --------------------ejercicio9----------------------

# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))
# n4 = float(input("Nota 4: "))

# notas = (n1, n2, n3, n4)

# print("Nota más alta:", max(notas))
# print("Nota más baja:", min(notas))

# ----------------------ejercicio10--------------------

# conversiones = {
#     "km": 1000,
#     "m": 1,
#     "cm": 0.01
# }


# unidad = input("Ingresa la unidad (km, m, cm): ")
# cantidad = float(input("Ingresa la cantidad: "))

# resultado = cantidad * conversiones[unidad]

# print("Equivalente en metros:", resultado)

# -------------------ejercicio11--------------

# p1 = float(input("Precio 1: "))
# p2 = float(input("Precio 2: "))
# p3 = float(input("Precio 3: "))

# precios = [p1, p2, p3]

# iva1 = p1 * 1.19
# iva2 = p2 * 1.19
# iva3 = p3 * 1.19

# precios_con_iva = [iva1, iva2, iva3]

# print("Precios con IVA:", precios_con_iva)

# ---------------------ejercicio12------------------

# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))

# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2 

# operaciones = (suma, resta, multiplicacion, division)

# print("Resultados (suma, resta, multiplicación, división):", operaciones)

# --------------ejercicio13----------

# nombre1 = input("Nombre 1: ")
# nota1 = float(input("Nota 1: "))

# nombre2 = input("Nombre 2: ")
# nota2 = float(input("Nota 2: "))

# nombre3 = input("Nombre 3: ")
# nota3 = float(input("Nota 3: "))

# estudiantes = {
#     nombre1: nota1,
#     nombre2: nota2,
#     nombre3: nota3
# }

# promedio = (nota1 + nota2 + nota3) / 3

# print(estudiantes)
# print("Promedio general:", promedio)

# -----------------ejercicio14-------------------

# s1 = float(input("Salario 1: "))
# s2 = float(input("Salario 2: "))
# s3 = float(input("Salario 3: "))
# s4 = float(input("Salario 4: "))
# s5 = float(input("Salario 5: "))

# nuevo1 = s1 * 1.10
# nuevo2 = s2 * 1.10
# nuevo3 = s3 * 1.10
# nuevo4 = s4 * 1.10
# nuevo5 = s5 * 1.10

# nuevos_salarios = [nuevo1, nuevo2, nuevo3, nuevo4, nuevo5]

# print("Nuevos salarios:", nuevos_salarios)

#-------------------------ejercicio15--------------------

# productos = {
#     "producto1": 1000,
#     "producto2": 2000,
#     "producto3": 3000
# }

# impuesto = input("Ingresa el porcentaje de impuesto: ")
# imp = float(impuesto) / 100

# precio1 = productos["producto1"] + productos["producto1"] * imp
# precio2 = productos["producto2"] + productos["producto2"] * imp
# precio3 = productos["producto3"] + productos["producto3"] * imp

# productos_finales = {
#     "producto1": precio1,
#     "producto2": precio2,
#     "producto3": precio3
# }

# print("Precios finales con impuesto:")
# print(productos_finales)

# -------------------------ejercicio16-------------------------

# e1 = int(input("Edad 1: "))
# e2 = int(input("Edad 2: "))
# e3 = int(input("Edad 3: "))
# e4 = int(input("Edad 4: "))
# e5 = int(input("Edad 5: "))

# mayores = (e1 >= 18) + (e2 >= 18) + (e3 >= 18) + (e4 >= 18) + (e5 >= 18)

# menores = 5 - mayores

# print("Mayores de edad:", mayores)
# print("Menores de edad:", menores)

# -----------------ejercicio17--------------------

dolares = float(input("Ingresa una cantidad en dólares: "))

euro = 0.85
peso = 3900
yen = 110.2

conversion = (dolares * euro, dolares * peso, dolares * yen)

print("Tupla de conversiones:", conversion)