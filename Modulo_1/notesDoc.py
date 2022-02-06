from datetime import date

# Variables

sum = 1 + 2
product = sum * 2
print(product)

# Fechas

date = date.today()
print("Today's date is: " + str(date))

# Entrada de usuario

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Entrada de usuario con numeros

print("Calculadora")
first_number = int(input("Primer número: "))
second_number = int(input("Segundo número: "))
print(first_number + second_number)
