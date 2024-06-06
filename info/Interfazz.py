import tkinter as tk
from tkinter import messagebox
from funciones import*
from funciones import mycursor
def ingresar():
    """ La función se encarga de validar el ingreso del usuario y contraseña.
    """
    user = entry_user.get().capitalize()
    passw = entry_pass.get()
    
    if Menu_ingreso(user, passw):
        messagebox.showinfo("Ingreso", "Ingresó correctamente al sistema")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

""" Se configura la iterfaz.
"""
ventana = tk.Tk()
ventana.title("Sistema de Ingreso")

""" Se crean los widgets y su distribución en la interfaz.
"""
tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
entry_user = tk.Entry(ventana)
entry_user.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
entry_pass = tk.Entry(ventana, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=10)

btn_ingresar = tk.Button(ventana, text="Ingresar", command=ingresar)
btn_ingresar.grid(row=2, column=0, columnspan=2, pady=10)
""" Muestra en pantalla lo que ejecuta el codigo y permite la interacción con el usuario.
"""
ventana.mainloop()