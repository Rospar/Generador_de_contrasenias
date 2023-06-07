import random
import tkinter as tk
from werkzeug.security import generate_password_hash

def generar_contrasena():
    minus="abcdefghijklmnopqrstuvwxyz"
    mayus=minus.upper()
    Numeros="1234567890"
    longuitud=12
    simbolos="$,.-_:;{}[]{}´¨*'+<>\^`~¿?@!#%&/()=°||"
    muestra=random.sample(minus+mayus+simbolos+Numeros,longuitud)
    Password="".join(muestra)
    return Password

def encriptar_contrasena():
    encryptP=generate_password_hash(generar_contrasena())
    return encryptP

def mostrar_contrasenas():
    contrasena_entry.config(text=generar_contrasena())
    contrasena_encriptada_entry.config(text=encriptar_contrasena())


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de contraseñas")
ventana.geometry("500x500")

# Crear widgets
mostrar_btn = tk.Button(ventana, text="Generar", command=mostrar_contrasenas)
mostrar_btn.pack()
contrasena_label = tk.Label(ventana, text="Contraseña generada:")
contrasena_entry = tk.Label(ventana,text="")


contrasena_encriptada_label = tk.Label(ventana, text="Contraseña encriptada:")
contrasena_encriptada_entry = tk.Label(ventana, text="")

# Posicionar los widgets en la ventana
contrasena_label.pack()
contrasena_entry.pack()

contrasena_encriptada_label.pack()
contrasena_encriptada_entry.pack()

# Ejecutar la aplicación
ventana.mainloop()
