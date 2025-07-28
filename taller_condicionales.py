#Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor (65+)

# edad = int(input("¿Cuantos años tienes? "))

# if edad < 18:
#     print("Eres menor de edad")
# elif edad >= 65:
#     print("Eres adulto mayor")
# else:
#     print("Eres mayor de edad")

#2. Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo; 
# entre 1.5 y 1.8 m, estatura media; mas de 1.8 m, alto.

# estatura = float(input("¿Cuanto mides? "))

# if estatura < 1.5:
#     print("Eres bajito")
# elif estatura <= 1.8:
#     print("Tienes una estatura normal")
# else:
#     print("Eres alto")

#3. Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.

# num = int(input("ingrese un número: "))

# if num % 2 == 0:
#     print("Es múltiplo de 2")
# elif num % 3 == 0:
#     print("Es múltiplo de 3")
# else:
#     print("No es múltiplo ni de 2 ni de 3")

#4. Pide un numero decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

# num = input("Escribe un numero decimal: ")
# partes = num.split(".")

# if len(partes) == 1:
#     print("No tiene decimales")
# else:
#     decimales = partes[1]
#     if len(decimales) == 1:
#         print("Tiene 1 decimal")
#     elif len(decimales) == 2:
#         print("Tiene 2 decimales")
#     else:
#         print("Tiene más de 2 decimales")

#5 Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

# pais = input("Escribe un pais: ")
# paises = ("Colombia", "Perú", "Argentina", "México")

# if pais in paises:
#     print("Ese pais sí está en la lista")
# else:
#     print("Ese pais no está en la lista")

#6. Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

# tipo = input("¿Cual es tu tipo de sangre? (A, B, AB, O): ")
# compatibilidad = {
#     "A": "puedes recibir de A y O",
#     "B": "puedes recibir de B y O",
#     "AB": "puedes recibir de todos (A, B, AB, O)",
#     "O": "solo puedes recibir de O"
# }

# if tipo in compatibilidad:
#     print("Segun tu tipo de sangre,", compatibilidad[tipo])
# else:
#     print("Tipo de sangre no valido")

#7. Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.

# temp = float(input("¿Cuantos grados hace (°C)? "))

# if temp < 10:
#     print("Hace frio")
# elif temp <= 25:
#     print("Esta templado")
# else:
#     print("Hace calor")

#8. Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada.

# print("Menu")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")

# opcion = input("Elige una opcion (1, 2 o 3): ")

# num1 = float(input("Escribe el primer numero: "))
# num2 = float(input("Escribe el segundo numero: "))

# if opcion == "1":
#     print("La suma es:", num1 + num2)
# elif opcion == "2":
#     print("La resta es:", num1 - num2)
# elif opcion == "3":
#     print("La multiplicacion es:", num1 * num2)
# else:
#     print("Opcion no valida")

#9. Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.

# mes_num = input("Escribe un numero del 1 al 12: ")

# meses = {
#     "1": "Enero",
#     "2": "Febrero",
#     "3": "Marzo",
#     "4": "Abril",
#     "5": "Mayo",
#     "6": "Junio",
#     "7": "Julio",
#     "8": "Agosto",
#     "9": "Septiembre",
#     "10": "Octubre",
#     "11": "Noviembre",
#     "12": "Diciembre"
# }

# if mes_num in meses:
#     print("El mes es:", meses[mes_num])
# else:
#     print("Numero no valido")

#10. Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro.

# num = input("Escribe un numero de 4 digitos: ")

# if num[0] == "1":
#     print("Empieza con 1")
# elif num[0] == "2":
#     print("Empieza con 2")
# else:
#     print("Empieza con otro numero")

#11. Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un número.

# palabra = input("Escribe una palabra: ")
# primera = palabra[0]

# vocales = "aeiouAEIOU"
# numeros = "0123456789"

# if primera in vocales:
#     print("Empieza con vocal")
# elif primera in numeros:
#     print("Empieza con un numero")
# else:
#     print("Empieza con una consonante")

#12. Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible.

# fruta = input("Escribe una fruta: ")

# precios = {
#     "manzana": "2000 pesos",
#     "pera": "1800 pesos",
#     "piña": "2500 pesos"
# }

# if fruta in precios:
#     print("El precio de la", fruta, "es", precios[fruta])
# else:
#     print("Esa fruta no esta disponible")

#13. Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente.

# nota = float(input("Escribe tu calificacion (de 0 a 5): "))

# if nota < 3:
#     print("no paso")
# elif nota <= 4:
#     print("paso")
# else:
#     print("Excelente")

#14. Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

# num = int(input("Escribe un numero: "))

# if num % 4 == 0:
#     print("se puede dividir entre 4")
# elif num % 6 == 0:
#     print("se puede dividir entre 6")
# else:
#     print("No se puede dividir entre 4 ni entre 6")

#15. Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar

# usuarios = {
#     "esteban": "1234",
#     "anderson": "abcd",
#     "santiago": "pass"
# }

# usuario = input("Usuario: ")
# clave = input("Clave: ")

# if usuario in usuarios and usuarios[usuario] == clave:
#     print("Acceso permitido")
# else:
#     print("Usuario o clave incorrectos")

#16. Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+).

# edad = int(input("Escribe tu edad: "))

# if edad >= 0 and edad <= 12:
#     print("Eres un niño")
# elif edad <= 17:
#     print("Eres un adolescente")
# elif edad <= 64:
#     print("Eres un adulto")
# else:
#     print("Eres un adulto mayor")

#17. Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.

# ciudad = input("Escribe el nombre de una ciudad: ")
# capitales = ("Bogota", "Lima", "Quito", "Caracas")

# if ciudad in capitales:
#     print("Es una capital")
# else:
#     print("Ciudad secundaria")

#18. Ingresa el valor de una compra. Si es mayor de $200.000
# aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

# valor = float(input("Escribe el valor de la compra: "))

# if valor > 200000:
#     descuento = valor * 0.15
#     total = valor - descuento
#     print("Descuento del 15%")
# elif valor >= 100000:
#     descuento = valor * 0.10
#     total = valor - descuento
#     print("Descuento del 10%")
# else:
#     descuento = 0
#     total = valor
#     print("No hay descuento")

# print("Total a pagar:", total)

#19. Pide el nombre y el número de horas trabajadas. Calcula el salario 
#con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

# nombre = input("Escribe tu nombre: ")
# horas = int(input("Cuantas horas trabajaste: "))

# tarifa = 10000
# salario = horas * tarifa

# if horas > 40:
#     bono = salario * 0.20
#     salario = salario + bono
#     print("Tienes un bono del 20%")

# print(f"Hola {nombre}, tu salario es: {salario}")

#20. Ingresa tu puntaje en una 
#prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente

# puntaje = int(input("Cuanto sacaste en la prueba (0 a 100): "))

# if puntaje < 50:
#     print("Te fue mal")
# elif puntaje <= 79:
#     print("Pasaste raspando")
# else:
#     print("Te fue super bien") 
