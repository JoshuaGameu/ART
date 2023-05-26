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

# Factor de estabilización γ
gamma = 0.5

# Parámetro de vigilancia ρ
rho = 0.8

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

# Función para calcular V∗(t+1)
def calcular_V_estrella(V, E, W, gamma):
    N = len(E)
    sigma = np.sum([V[0][j] * E[j] for j in range(N)])
    V_estrella = gamma + sigma / N
    return V_estrella

# Actualizar matrices de pesos con el primer vector de entrada
V_estrella = calcular_V_estrella(V, E1, W, gamma)
V = np.vstack((V, E1 * V_estrella))
W = np.vstack((W, np.zeros(N+1)))

# Imprimir matrices de pesos antes de la actualización
print("Matriz V antes de la actualización:")
print(np.around(V, decimals=2))
print("Matriz W antes de la actualización:")
print(np.around(W, decimals=2))

# Actualizar matrices de pesos con el segundo vector de entrada
V_estrella = calcular_V_estrella(V, E2, W, gamma)
V = np.vstack((V, E2 * V_estrella))
W = np.vstack((W, np.zeros(N+1)))

# Imprimir matrices de pesos después de la actualización
print("Matriz V después de la actualización:")
print(np.around(V, decimals=2))
print("Matriz W después de la actualización:")
print(np.around(W, decimals=2))

# Calcular semejanza entre E1 y E3
Rs = np.dot(E3, V[1]) / np.sum(E3)

# Comparar semejanza con el parámetro de vigilancia
if Rs > rho:
    # E3 pertenece a la misma clase
    V_estrella = calcular_V_estrella(V, E3, W, gamma)
    V = np.vstack((V, E3 * V_estrella))
    W = np.vstack((W, np.zeros(N+1)))
else:
    # Crear nueva clase para E3
    M += 1
    V_estrella = calcular_V_estrella(V, E3, W, gamma)
    V = np.vstack((V, E3 * V_estrella))
    W = np.vstack((W, np.zeros(N+1)))
    W[-1][-1] = 0.28

# Imprimir matrices de pesos después de la actualización
print("Matriz V después de la actualización:")
print(np.around(V, decimals=2))
print("Matriz W después de la actualización:")
print(np.around(W, decimals=2))
