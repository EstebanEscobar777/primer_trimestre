# frutas=[]
# print (frutas)

# frutasp=input ("ingrese la primera fruta: ")
# frutasp1=input ("ingrese la segunda fruta: ")
# frutasp2=input ("ingrese la tercera fruta: ")
# frutas. append(frutasp)
# frutas. append(frutasp1)
# frutas. append(frutasp2)


# print (frutas)

#--------------------------------------------------------------


# edades=[]
# print (edades)

# edad=int (input("ingrese la primera edad: "))
# edad1=int (input("ingrese la segunda edad: "))

# edades. append(edad)
# edades. append(edad1)


# print (edades)

# #----------------------------------------------------------------------


# notas=[]
# print (notas)

# nota=float (input("ingrese la primera nota: "))
# nota1=float (input("ingrese la segunda nota: "))

# ope=nota+nota1
# ope1= ope/2

# notas. append(edad)
# notas. append(edad1)


# print (notas)
# print (f"el promedio de las notas es: {ope1}")

#---------------------------------------------------------

# productos=[]
# print (productos)

# producto=input ("ingrese el primera producto: ")
# producto2=input ("ingrese el segunda producto: ")
# producto3=input ("ingrese el tercera producto: ")
# productos. append(producto)
# productos. append(producto2)
# productos. append(producto3)


# print (productos)

#---------------------------------------------------------------

# Precios=[]


# articulo=float (input("ingrese el primer articulo: "))
# articulo2=float (input("ingrese el segundo articulo: "))
# articulo3=float (input("ingrese el tercer articulo: "))

# ope=articulo+articulo2+articulo3


# Precios. append(articulo)
# Precios. append(articulo2)
# Precios. append(articulo3)


# print (Precios)
# print (f"la suma total de los articulos es {ope}")

# -------------------------ejercicio6----------------------------

# numeros=[]

# numero=int (input("ingrese el primer num: "))
# numero1=int (input("ingrese el segundo numero: "))
# numero2=int (input("ingrese el tercer numero: "))
# numero4=int (input("ingrese el cuarto numero: "))

# numeros.append(numero)
# numeros.append(numero1)
# numeros.append(numero2)
# numeros.append(numero4)

# print (f"el numero mayor es {max(numeros)} y el numero menor es {min(numeros)}")

# -----------------------ejercicio7----------------------------

# nombres=[]

# nombre=input ("ingresa el primer nombre: ")
# nombre2=input ("ingrese el segundo nombre: ")

# nombres.append(nombre)
# nombres.append(nombre2)

# print(nombres)
# print(f"hola {nombre}, hola {nombre2}")

# --------------------------ejercicio8------------------------

# temperatura=[]

# temp=float (input("ingrese la primer temperatura: "))
# temp2=float (input("ingrese la segunda temperatura: "))

# ope=temp*9/5+32
# ope2=temp2*9/5+32

# print(f"el resultado del primero en fahrenheit es {ope} y del segundo es {ope2}")

# ---------------------------------------

# frutas=['manzana','banana','naranja','banana']
# frutas=[]
# frutas.remove('banana')
# print(frutas)

# -----------------------ejercicio1----------------------1

# num=[]
# num.append(7)
# print(num)

# -----------------------ejercicio2----------------------

# nombres=["ana","luis"]
# nombres.append("calos")
# print(nombres)

# ----------------------ejercicio1------------------------2

# numeros=[1,2,3]
# numeros.insert(0,"99")
# print (numeros)

# ---------------------------ejercicio2---------------------

# colores=["azul","verde"]
# colores.insert(1,"rojo")
# print (colores)

# -------------------------------ejercicio1--------------------3

# lista=[1,2,3]
# lista.extend([4,5,6])
# print(lista)

# ---------------------------ejercicio2---------------------

# letras=['a','b']
# letras.extend('ok')
# print (letras)

# -------------------------ejercicio1--------------4

# frutas=['manzana','uva','pera']
# frutas.remove('uva')
# print(frutas)

# ------------------------ejercicio2--------------------

# num=[1,2,3,2]
# num.remove(2)
# print(num)

# --------------------ejercicio1----------------------------5

# lista=[1,2,3,4]
# valor=lista.pop()
# print(valor)
# print(lista)

# ------------------ejercicio2--------------------------

# lista=["uno","dos","tres"]
# valor=lista.pop(0)
# print(valor)
# print(lista)

# -----------ejercicio1--------------------6

# lista=[1,2,3]
# lista.clear()
# print(lista)

# ------------------ejercicio2---------------

# lista=[1,"dos",3,"cuatro"]
# lista.clear()
# print(lista)

# ------------------ejercicio1------------------7

# frutas=["manzana","pera","uva"]

# print(frutas.index("pera"))

# --------------------ejercicio2--------------------

# numeros=[4,5,6,7]

# print(numeros.index(6))

# -----------------ejercicio1-------------------8

# numeros=[3,1,3,5,3]

# print(numeros.count(3))

# -------------ejercicio2-----------------

# lista=["a","b","a","c","a"]
# print(lista.count("a"))

# ---------------------ejercicio1---------------9

# lista=[5,1,4,2,3]
# lista.sort()
# print(lista)

# ------------------ejercicio2-------------------

# lista=["z","a","m","b"]
# lista.sort()
# print(lista)

# --------------------ejercicio1-----------------10

# lista=[1,2,3,4]
# lista.reverse()
# print(lista)

# ----------------------ejercicio2-------------------

# lista=["inicio","medio","fin"]
# lista.reverse()
# print(lista)

# --------------------ejercicio1------------------11

# lista=[1,2,3]
# nueva=lista.copy()
# nueva.append(lista)
# print(nueva)

# ---------------------ejercicio2-----------------

# lista=["a","b","c"]
# nueva=lista.copy()
# nueva.append("d")
# print(lista)
# print(nueva)

# ----------------actividad--------------------

lista1=[]
lista2=[]
lista1.append(100)
lista1.append("hola mundo")
lista2.append(300)
lista2.append("hola y adios")
lista3=lista1.copy()
lista3.remove("hola mundo")
lista4=lista2.copy()
lista4.remove("hola y adios")
lista4.remove(300)
lista5=[]
lista5.extend(lista4)
lista5.extend(lista3)
print(f"lista 1 {lista1}")
print(f"lista 2 {lista2}")
print(f"lista 3 {lista3}")
print(f"lista 4 {lista4}")
print(f"lista 5 {lista5}")