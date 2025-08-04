# numero= 32
# if numero > 40:
#     print("el numero es >")
# else:
#     print("es <")
# print("fin")

# edad=int(input("ingresa edad"))

# if edad < 0:
#     print("no cumple")
# elif edad <= 17:
#     print ("< de edad")
# elif edad >= 18:
#     print ("> de edad")
# elif edad <= 101:
#     print ("se nos fue")
# else:
#     print ("edad no existe")


# ---------ejercicio----------

# v=input("ingrese vocal en minuscula: ")
# if v == "a":
#     print("A")
# elif v == "e":
#     print ("E")
# elif v == "i":
#     print ("I")
# elif v == "o":
#     print ("O")
# elif v == "u":
#     print ("U")
# else:
#     print("no es una vocal minuscula")


#---------------taller practico if y que tales-------------------

# n=int(input("ingrese un numero: "))
# if n > 0:
#     print("es positivo")
# elif n < 0:
#     print("es negativo")
# else:
#     print("es cero")

#--------------ejercicio2-------------------------


# n1=int(input("coloque el primer numero: "))
# n2=int(input("coloque el segundo numero: "))
# if n1 > n2:
#     print(f"el mayor es: {n1}")
# else:
#     print(f"el mayor es: {n2}")

#------------ejercicio3-------------------

# n=int(input("ingrese numero: "))
# if n % 2 == 0:
#     print("es par")
# else:
#     print("es impar")

#-------------------ejercicio4-----------------

# n=int(input("ingrese un numero: "))
# if n >= 10 and n <= 20:
#     print("esta entre 10 y 20")
# else:
#     print("no esta entre 10 y 20")
    

#------------------------ejercicio5-------------------

# a=int(input("ingrese el primer numero: "))
# b=int(input("ingrese el segundo numero: "))
# c=int(input("ingrese el tercer numero: "))
# if a >= b and a >= c:
#     print(f"el mayor es: {a}")
# elif b >= a and b >= c:
#     print(f"el mayor es: {b}")
# else:
#     print(f"el mayor es: {c}")

#------------------ejercicio6-------------------

# sa=float(input("ingrese el total de la compra: "))
# if sa > 100:
#     sa = sa * 0.9
# print(f"total a pagar: {sa}")

#-------------ejercicio7--------------------

# edad = int(input("ingrese edad: "))
# if edad >= 18:
#     print("puede votar")
# else:
#     print("no puede votar")

#---------------ejercicio8-------------

# wa=float(input("precio: "))
# tipo = input("tipo de cliente (VIP o normal): ")
# if tipo == "VIP":
#     wa == wa * 0.8
# print (f"total a pagar {wa}")

#--------------ejercicio9------------------

# num=int(input("ingrese numero: "))
# if num % 5 == 0 and num % 3 == 0:
#     print("es multiplo de 5 y de 3")
# else: 
#     print("no es multiplo de 5 y 3")


#----------------ejercicio10-------------

# num=int(input("ingrese un numero: "))
# a=int(input("divisor 1: "))
# b=int(input("divisir 2: "))
# if num % a == 0 and num % b == 0:
#     print("es divisible entre los dos")
# else:
#     print("no es divisible entre los dos")

# ----------------ejercicio11------------

# num = [5, 12, 9, 8, 4]
# if num[2] > 10:
#     print("Mayor a 10")
# else:
#     print("Menor o igual a 10")

#-------------ejercicio12---------------

# lista = [3, 5, 7, 9]
# if 7 in lista:
#     print("Está en la lista")
# else:
#     print("No está en la lista")

#---------------ejercicio13----------------

# lista = [4, 6, 2, 8]
# suma = lista[0] + lista[1]
# if suma > 10:
#     print("Suma alta")
# else:
#     print("Suma baja")

#-----------ejercicio14-----------------

# nombres = ["Ana", "Luis", "Pedro", "Marta"]
# ultimo = nombres[-1]
# if ultimo == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")

#-------------ejercicio15----------------

# colores = ["rojo", "azul", "verde"]
# if colores[1] == "azul":
#     colores[1] = "amarillo"
# print(colores)

#--------------ejercicio16----------------

# valores = (5, 8, 12, 20)
# if valores[0] < valores[-1]:
#     print("Orden ascendente")
# else:
#     print("Orden descendente")

#---------------ejercicio17----------------

# tupla = (25, 32, 28)
# if tupla[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")

#-----------------ejercicio18-------------

# t = (1, 2, 3)
# lista = list(t)
# if lista[1] == 2:
#     lista[1] = 10
# t = tuple(lista)
# print(t)

#---------------ejericio19---------------

# coord = (4, 9)
# if coord[1] > 5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

#--------------ejercicio20----------------

# t1 = (3, 4)
# t2 = (3, 5)
# if t1 == t2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")

#----------------ejercicio21-----------------

# persona = {"nombre": "Juan", "edad": 17}
# if persona["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

#---------------ejercicio22----------------

# persona = {"nombre": "Lucia", "edad": 20}
# if persona["edad"] > 18:
#     persona["edad"] = 21
# print(persona)

#--------------ejercicio23-----------------

# persona = {"nombre": "Carlos"}
# if "ciudad" not in persona:
#     persona["ciudad"] = "Bogotá"
# print(persona)

#----------------ejercicio24---------------

# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")

#---------------ejercicio25----------------

# inventario = {"pan": 1200, "leche": 2000}
# if "pan" in inventario:
#     print(inventario["pan"])
# else:
#     print("Producto no disponible")


