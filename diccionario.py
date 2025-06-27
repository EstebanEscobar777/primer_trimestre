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

frutas={

"uva": "precio por kilo 2000",
"pera":"precio por kilo 3000",
"sandia": "precio por kilo 5000"


}

print(frutas)




# print(frutas)