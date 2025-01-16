num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

# definir el operadorr

operador = input("Introduce la operacion a realizar (suma, resta, multiplicacion, division): ")

resultado = 0

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'multiplicacion':
    resultado = num1 * num2
elif operador == 'division':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: No se puede dividir por cero"
else:
    resultado = "Operacion no valida"

print("El resultado es", resultado)
