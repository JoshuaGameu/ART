import numpy as np

# Valores de M y N
M = 2  # Cantidad de neuronas de salida
N = 4  # Cantidad de neuronas de entrada

# Vectores de entrada
E1 = np.array([1, 1, 0, 1])
E2 = np.array([0, 0, 1, 1])
E3 = np.array([1, 1, 1, 0])

# Inicializar matrices de pesos
V = np.ones((1, N))
W = np.ones((M, N+1)) * (1 / (1 + N))

# Función para normalizar el vector de entrada
def normalizar_vector(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

# Normalizar vectores de entrada
E1 = normalizar_vector(E1)
E2 = normalizar_vector(E2)
E3 = normalizar_vector(E3)

# Actualizar matrices de pesos con el primer vector de entrada
V = np.vstack((V, E1))
W = np.vstack((W, np.zeros(N+1)))

# Imprimir matrices de pesos antes de la actualización
print("Matriz V antes de la actualización:")
print(V)
print("Matriz W antes de la actualización:")
print(W)

# Actualizar matrices de pesos con el segundo vector de entrada
V = np.vstack((V, E2))
W = np.vstack((W, np.zeros(N+1)))

# Imprimir matrices de pesos después de la actualización
print("Matriz V después de la actualización:")
print(V)
print("Matriz W después de la actualización:")
print(W)

# Actualizar matrices de pesos con el tercer vector de entrada
V = np.vstack((V, E3))
W = np.vstack((W, np.zeros(N+1)))

# Imprimir matrices de pesos después de la actualización
print("Matriz V después de la actualización:")
print(V)
print("Matriz W después de la actualización:")
print(W)
