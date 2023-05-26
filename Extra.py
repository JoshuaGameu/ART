import tkinter as tk
import numpy as np

frame_list = []
matrix_list = []
matrices_entrenamiento = []

def create_grid(frame, matrix, matrix_label):
    canvas = tk.Canvas(frame, width=200, height=200)
    canvas.pack(padx=10, pady=10)  # Agregar un margen interno al canvas

    rects = []  # Almacenar los rectángulos

    for i in range(4):
        for j in range(4):
            rect = canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill="white")
            matrix[j][i] = 0  # Inicializar matriz con ceros
            rects.append(rect)  # Agregar el rectángulo a la lista

            def change_color(event, i=i, j=j):
                nonlocal matrix
                current_color = canvas.itemcget(tk.CURRENT, "fill")
                if current_color == "white":
                    canvas.itemconfig(tk.CURRENT, fill="red")
                    matrix[j][i] = 1
                else:
                    canvas.itemconfig(tk.CURRENT, fill="white")
                    matrix[j][i] = 0

            canvas.tag_bind(rect, "<Button-1>", change_color)

    def show_matrix():
        matrix_str = ""
        for i in range(4):
            row_str = ", ".join([str(x) for x in matrix[i]])
            matrix_str += row_str + "\n"
        matrix_label.config(text="Matriz:\n" + matrix_str)

    def entrenar():
        matrix_list[frame_list.index(frame)] = matrix.copy()
        matrices_entrenamiento.append(matrix.copy())
        show_matrix()
        print("Matriz entrenada:", matrix)

    def limpiar():
        nonlocal matrix
        matrix = np.zeros((4, 4), dtype=int)
        for rect in rects:
            canvas.itemconfig(rect, fill="white")
        matrix_label.config(text="Matriz:\n")
        show_matrix()

    show_button = tk.Button(frame, text="Mostrar Matriz", command=show_matrix)
    show_button.pack()
    entrenar_button = tk.Button(frame, text="Entrenar", command=entrenar)
    entrenar_button.pack()
    limpiar_button = tk.Button(frame, text="Limpiar", command=limpiar)
    limpiar_button.pack()
    matrix_label.pack()

root = tk.Tk()
root.title("Cambiar Color")

canvas_frame = tk.Frame(root)  # Frame para el canvas
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Ajustar al contenido y agregar margen interno

for _ in range(4):
    frame = tk.Frame(canvas_frame)  # Frame para cada cuadrícula
    frame.pack(side=tk.LEFT, padx=10)

    matrix = np.zeros((4, 4), dtype=int)
    matrix_label = tk.Label(frame, text="Matriz:\n")
    create_grid(frame, matrix, matrix_label)

    frame_list.append(frame)
    matrix_list.append(matrix)

root.mainloop()
