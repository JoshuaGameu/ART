# Importar la biblioteca numpy para realizar cálculos numéricos
import numpy as np

# Definir la función para calcular el centroide de la salida
def centroide_defuzzificacion(mf, x):
    # Calcula el centro de masa ponderado de la función de membresía
    return np.sum(mf * x) / np.sum(mf)

# Solicitar al usuario la cantidad de funciones de membresía y los valores de entrada
num_mf = int(input("Ingrese el número de funciones de membresía: "))
x_values = input("Ingrese los valores de entrada separados por comas: ").split(",")
x_values = [float(x.strip()) for x in x_values]

# Inicializar la matriz de funciones de membresía y la matriz de salida
mf_matrix = np.zeros((num_mf, len(x_values)))
out_matrix = np.zeros((num_mf, len(x_values)))

# Solicitar al usuario las funciones de membresía para cada entrada
for i in range(num_mf):
    mf_values = input("Ingrese los valores de la función de membresía %d separados por comas: " % (i+1)).split(",")
    mf_values = [float(x.strip()) for x in mf_values]
    mf_matrix[i,:] = mf_values

# Calcular la salida para cada valor de entrada
for i in range(len(x_values)):
    out_matrix[:,i] = mf_matrix[:,i] * x_values[i]

# Calcular el centroide de la salida
out_centroid = centroide_defuzzificacion(out_matrix, x_values)

# Imprimir el resultado del centroide de la salida
print("El centroide de la salida es: ", out_centroid)
