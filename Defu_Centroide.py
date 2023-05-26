def defuzzificacion_centroide(membresias, valores):
    # Calcula el centro de masa ponderado
    numerador = sum(membresias[i] * valores[i] for i in range(len(membresias)))
    denominador = sum(membresias)
    centroide = numerador / denominador
    
    return centroide
# Definir funciones de membresía y valores correspondientes
membresias = [0.2, 0.5, 0.8, 0.5, 0.2]
valores = [10, 20, 30, 40, 50]

# Calcular el centroide de la salida
centroide = defuzzificacion_centroide(membresias, valores)

# Imprimir el resultado
print("El valor del centroide es:", centroide)

