# Definir la función de defuzzificación por centroide
def defuzzificacion_centroide(membresias, valores):
    # Calcula el centro de masa ponderado
    numerador = sum(membresias[i] * valores[i] for i in range(len(membresias)))
    denominador = sum(membresias)
    centroide = numerador / denominador
    
    return centroide

# Pedir al usuario que ingrese los valores de entrada y los pesos correspondientes
valores = input("Ingresa los valores de entrada separados por comas: ")
valores = [float(valor.strip()) for valor in valores.split(",")]
pesos = input("Ingresa los pesos correspondientes separados por comas: ")
pesos = [float(peso.strip()) for peso in pesos.split(",")]

# Imprimir los valores de entrada y los pesos correspondientes
print("Valores de entrada:", valores)
print("Pesos correspondientes:", pesos)

# Pedir al usuario que ingrese el número de funciones de membresía y sus valores
num_membresias = int(input("Ingresa el número de funciones de membresía: "))
membresias = []
for i in range(num_membresias):
    funcion = input("Ingresa la función de membresía #" + str(i+1) + ": ")
    membresias.append([float(x.strip()) for x in funcion.split(",")])

# Imprimir las funciones de membresía
print("Funciones de membresía:")
for i in range(len(membresias)):
    print("Membresía #" + str(i+1) + ":", membresias[i])

# Calcular la función de pertenencia resultante
pertenencia = [min(membresias[j][i] for j in range(num_membresias)) for i in range(len(valores))]

# Imprimir la función de pertenencia resultante
print("Función de pertenencia resultante:", pertenencia)

# Calcular el centroide de la salida
centroide = defuzzificacion_centroide(pertenencia, valores)

# Imprimir el resultado
print("El valor del centroide es:", centroide)
