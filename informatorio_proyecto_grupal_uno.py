import tkinter as tk
from tkinter import ttk
import time

# Main window setup

ventana = tk.Tk()
ventana.title('Grupo 10')
ventana.geometry('600x450')
ventana.resizable(False, False)
ventana.config(bg="#f4f4f4")

# FUNCIONES
def agregar_al_carrito(texto):
    ventana_carrito.insert(tk.END, texto)

def agregar_producto_al_carrito(texto):
    agregar_al_carrito(texto)

def eliminar_producto():
    seleccion = ventana_carrito.curselection()
    if seleccion:
        ventana_carrito.delete(seleccion)
        
def canc_ped():
    combobox.set("")
    ventana_carrito.delete(0,tk.END)

def agregar_producto():
    tarea = combobox.get()
    if tarea:
        agregar_al_carrito(tarea)

def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

def ventan_ped():
    #ventana.withdraw()
    ventana_p = tk.Tk()
    ventana_p.title('Pedidos')
    ventana_p.geometry('500x350')
    ventana_p.resizable(False, False)
    ventana_p.config(bg="#f4f4f4")
  
    def cerrar_ventana_ped():
        ventana_p.withdraw()
        combobox.set("")
        ventana_carrito.delete(0,tk.END)

    label_titulo=tk.Label(ventana_p, text="GRACIAS POR SU COMPRA!")
    label_titulo.config(font="Helvetica 20 ")
    label_titulo.place(x=45,y=20)
    
    marco2 = tk.Frame(ventana_p, bg='white', relief=tk.RAISED, borderwidth=1)
    marco2.place(x=20, y=70, width=450, height=200)

    scrollbar2 = tk.Scrollbar(marco2)
    scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
    
    venta_label=tk.Label(marco2,text= ventana_carrito.get(0,tk.END),
                          font=('Helvetica', 15), bg='#ffffff', fg='#333')
    venta_label.pack(side=tk.LEFT)

        ####BOTONES 2####
    boton_finalizar = tk.Button(ventana_p, text="Finalizar",
                               font=('Helvetica', 12), 
                               bg='red', fg='white', 
                               relief=tk.RAISED, borderwidth=1,
                               command=quit)
    boton_finalizar.place(x=285, y=285, width=130, height=30)
    
    boton_inicio = tk.Button(ventana_p, text="Inicio",
                               font=('Helvetica', 12), 
                               bg='blue', fg='white', 
                               relief=tk.RAISED, borderwidth=1,
                               command=cerrar_ventana_ped)
    boton_inicio.place(x=50, y=285, width=130, height=30)

    ventana_p.mainloop()




####    Main Menu    ####
barra_menu = tk.Menu(ventana, bg="#2e2e2e", fg="white")
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu, bg="#2e2e2e", fg="white", tearoff=0)
barra_menu.add_cascade(label='Menú', menu=menu_principal)

# Menu for Panchos
submenu_panchos = tk.Menu(menu_principal, bg="#2e2e2e", fg="white", tearoff=0)
menu_principal.add_cascade(label='Panchos', menu=submenu_panchos)
submenu_panchos.add_command(label='Tradicional', command=lambda: agregar_producto_al_carrito('Pancho tradicional'))
submenu_panchos.add_command(label='Con papas', command=lambda: agregar_producto_al_carrito('Pancho con papas'))

# Menu for Hamburguesas
submenu_hamburguesas = tk.Menu(menu_principal, bg="#2e2e2e", fg="white", tearoff=0)
menu_principal.add_cascade(label='Hamburguesa', menu=submenu_hamburguesas)
submenu_hamburguesas.add_command(label='De ternera', command=lambda: agregar_producto_al_carrito('Hamburguesa de ternera'))
submenu_hamburguesas.add_command(label='Vegetariana', command=lambda: agregar_producto_al_carrito('Hamburguesa vegetariana'))
submenu_hamburguesas.add_command(label='De pollo', command=lambda: agregar_producto_al_carrito('Hamburguesa de pollo'))

# Menu for Combos
submenu_combos = tk.Menu(menu_principal, bg="#2e2e2e", fg="white", tearoff=0)
menu_principal.add_cascade(label='Combos', menu=submenu_combos)
submenu_combos.add_command(label='Pancho tradicional + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Pancho tradicional + Gaseosa'))
submenu_combos.add_command(label='Pancho con papas + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Pancho con papas + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa de ternera + Porción de Papas', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de ternera + Porción de Papas'))
submenu_combos.add_command(label='Hamburguesa de ternera + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de ternera + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa de ternera + Porción de Papas + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de ternera + Porción de Papas + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa vegetariana + Porción de Papas', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa vegetariana + Porción de Papas'))
submenu_combos.add_command(label='Hamburguesa vegetariana + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa vegetariana + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa vegetariana + Porción de Papas + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa vegetariana + Porción de Papas + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa de pollo + Porción de Papas', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de pollo + Porción de Papas'))
submenu_combos.add_command(label='Hamburguesa de pollo + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de pollo + Gaseosa'))
submenu_combos.add_command(label='Hamburguesa de pollo + Porción de Papas + Gaseosa', command=lambda: agregar_producto_al_carrito('Combo: Hamburguesa de pollo + Porción de Papas + Gaseosa'))


####    Simple Clock    ####
reloj = tk.Label(ventana, font=('Helvetica', 20), bg='#f4f4f4', fg='#333')
reloj.pack(anchor='ne', padx=10, pady=10)
hora()

# Scrollable Cart   
carrito_nom = tk.Label(ventana, text="Carrito:", font=('Helvetica', 14), bg='#f4f4f4', fg='#333')
carrito_nom.place(x=20, y=130)

marco = tk.Frame(ventana, bg='#e0e0e0', relief=tk.RAISED, borderwidth=1)
marco.place(x=20, y=160, width=550, height=200)

scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

####    Adicionales    ####
opciones = ["+Cheddar", "+Panceta", "+Cebolla", "+Tomate", "+Lechuga"]
combobox = ttk.Combobox(ventana, values=opciones, font=('Helvetica', 12))
combobox.set('')
combobox.place(x=20, y=50)

carrito_nom_adicionales = tk.Label(ventana, text="Adicionales:", font=('Helvetica', 14), bg='#f4f4f4', fg='#333')
carrito_nom_adicionales.place(x=20, y=20)

#### CARRITO
ventana_carrito = tk.Listbox(marco, font=('Helvetica', 15), bg='#ffffff', fg='#333', selectmode=tk.SINGLE)
ventana_carrito.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
ventana_carrito.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=ventana_carrito.yview)

####    BOTONES    ####
boton_agregar = tk.Button(ventana, text="Agregar adicional", 
                          font=('Helvetica', 12), 
                          bg='#4CAF50', fg='white', 
                          relief=tk.RAISED, borderwidth=1,
                          command=agregar_producto)
boton_agregar.place(x=20, y=80, width=130, height=30)

boton_eliminar = tk.Button(ventana, text="Eliminar producto", 
                           font=('Helvetica', 12), 
                           bg='#f44336', fg='white', 
                           relief=tk.RAISED, borderwidth=1,
                           command=eliminar_producto)
boton_eliminar.place(x=20, y=370, width=130, height=30)

boton_cancelar_ped = tk.Button(ventana, text="Cancelar pedido",
                               font=('Helvetica', 12), 
                               bg='red', fg='white', 
                               relief=tk.RAISED, borderwidth=1,
                               command=canc_ped)
boton_cancelar_ped.place(x=220, y=370, width=130, height=30)

boton_completar = tk.Button(ventana, 
                            text="Completar pedido", 
                            font=('Helvetica', 12), 
                            bg='#2196F3', fg='white', 
                            relief=tk.RAISED, borderwidth=1,
                            command=ventan_ped)
boton_completar.place(x=420, y=370, width=150, height=30)



####    Loop principal
ventana.mainloop()