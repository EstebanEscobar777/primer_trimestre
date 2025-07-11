#verifica si un numero es positivo, negativo o cero.
# num1=float(input("ingrese el numero que desee: "))
# if num1 > 0:
#     print("positivo")
# elif num1 < 0:
#     print("es negativo")
# else:
#     print("es cero")

#calcula el mayor de dos numeros ingresados 

# num1=float(input("ingrese el primer numero: "))
# num2=float(input("ingrese el segundo numero: "))
# if num1>num2:
#     print(F"el numero {num1} es mayor que {num2}")
# elif num2<num1:
#     print(F"el numero {num2} es mayor que {num1}")

#determina si un numero es par o impar

# num1=float(input("ingrese el numero que desee: "))
# if num1 == 0:
#     print ("el numero es cero y es par")
# elif num1 % 2 == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")

#4 dado un numero, verifica si esta entre 10 y 20.

# num1=float(input("ingrese el numero que desee: "))
# if 10 <= num1 <= 20:
#     print("el numero esta entre 10 y 20 ")
# else:
#     print("el numero no esta entre 10 y 20")

#5 dados tres numeros encuentra el mayor usando condicionales 

# num1=int(input("ingrese el primer numero: "))
# num2=int(input("ingrese el segundo numero: "))
# num3=int(input("ingrese el tercer numero: "))

# if num1 >= num2 and num1 >=num3:
#     print(f"el numero mayor es : {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"el numero mayor es: {num2}")
# else:
#     print(f"el numero mayor es: {num3}")

#6 calcula el precio final con un 10% de descuento si el total es mayor a $100

# total=float(input("ingresa el total de la compra: "))
# if total > 100:
#     descuento =total * 0.10
#     totalf= total - descuento
#     print(f"aplicaste un descuento de 10%. el precio final es: {totalf}")
# else:
#     print(f"no aplica el descuento. el precio final es: {total}")

#7 verifica si una persona puede votar (mayor o igual a 18 años)

# edad=int(input("ingrese su edad: "))
# if edad >= 18:
#     print("puedes votar")
# else:
#     print("no puedes votar")

#8 dado el precio y tipo de cliente (vip o normal), aplica un descuento del 20% solo a vip.

# precio = float(input("¿Cuánto cuesta? "))
# tipo = input("¿Eres cliente vip o normal? ")

# if tipo == "vip":
#     descuento = precio * 0.20
#     precio_final = precio - descuento
# else:
#     precio_final = precio

# print("Te queda en:", precio_final)

#9 determina si un numero es multiplo de 5 y de 3 al mismo tiempo.

# numero = int(input("Escribe un número: "))

# if numero % 5 == 0 and numero % 3 == 0:
#     print("Sí es múltiplo de 5 y de 3 al mismo tiempo")
# else:
#     print("No es múltiplo de 5 y de 3 a la vez")

#10 dado un numero, verifica si es divisible entre dos numeros dados.

numero = int(input("Escribe un número: "))
div1 = int(input("Escribe el primer número para dividir: "))
div2 = int(input("Escribe el segundo número para dividir: "))

if numero % div1 == 0 and numero % div2 == 0:
    print("Sí se puede dividir entre los dos.")
else:
    print("No se puede dividir entre los dos.")