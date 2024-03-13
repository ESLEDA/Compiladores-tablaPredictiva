from tkinter import scrolledtext
import tkinter as tk
from tablaPre5 import parse_input  

def analizar():
    
    entrance = text_area.get("1.0", tk.END).strip()
    resultado = parse_input(entrance)
    result_label.delete("1.0", tk.END)
    result_label.insert(tk.INSERT, resultado)
   

# Crear la ventana principal
root = tk.Tk()
root.title("TABLA PREDICTIVA")

# Crear el widget de entrada
lbl_entrada = tk.Label(root, text="Ingrese su cadena:", bg="lightblue")
lbl_entrada.pack(pady=20)

text_area = scrolledtext.ScrolledText(root,  height=5, bg="lightblue")
text_area.pack()
text_area.insert(tk.INSERT, "mientras(a < x)")


# botón para analizar
analyze_button = tk.Button(root, text="Analizar Cadena", command=analizar,bg="lightblue")
analyze_button.pack(pady=5)

# Crear el widget 
lbl_resultado = tk.Label(root)
lbl_resultado.pack(pady=10)

result_label = scrolledtext.ScrolledText(root, height=25, bg="lightblue")
result_label.pack(pady=10)


root.mainloop()
