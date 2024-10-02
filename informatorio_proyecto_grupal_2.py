import tkinter as tk
from tkinter import ttk
import time
from PIL import ImageTk, Image
# Variable para almacenar el producto actual y los adicionales
producto_actual = ""
#
crono_segundos = 5
#
c1 = True

# Main 
def main():
    ventana = tk.Tk()
    ventana.title('Grupo 10')
    ventana.geometry('600x450')
    ventana.resizable(False, False)
    ventana.config(bg="#f4f4f4")

    # FUNCIONES
  
    def agregar_al_carrito(texto):
        ventana_carrito.insert(tk.END, texto)
        actualizar_mensaje_adicionales(texto)
        mostrar_adicionales()

    def agregar_producto_al_carrito(texto):
        global producto_actual
        producto_actual = texto  
        agregar_al_carrito(texto)

    def agregar_adicional():
        global producto_actual
        adicional = combobox.get()
        if adicional and producto_actual: 
            producto_actual += f" {adicional}" 
            ventana_carrito.delete(tk.END)
            agregar_al_carrito(producto_actual)

    def eliminar_producto():
        seleccion = ventana_carrito.curselection()
        if seleccion:
            ventana_carrito.delete(seleccion)
        if ventana_carrito.size() == 0: 
            ocultar_adicionales()

    def canc_ped():
        combobox.set("")
        ventana_carrito.delete(0,tk.END)
        ocultar_adicionales()

    def agregar_producto():
        tarea = combobox.get()
        if tarea:
            agregar_al_carrito(tarea)

    def hora():
        tiempo_actual = time.strftime('%H:%M:%S')
        reloj.config(text=tiempo_actual)
        ventana.after(1000, hora)

    def ventan_ped():
        ventana.withdraw()
        ventana_p = tk.Tk()
        ventana_p.title('Pedidos')
        ventana_p.geometry('500x350')
        ventana_p.resizable(False, False)
        ventana_p.config(bg="#f4f4f4")

        label_titulo = tk.Label(ventana_p, text="GRACIAS POR SU COMPRA!")
        label_titulo.config(font="Helvetica 20 bold")
        label_titulo.pack(side="top")

        def crono_pedido():
            global crono_segundos
            if crono_segundos > 0:
                minutos, segundos = divmod(crono_segundos, 60)
                cronometro_pedido.config(
                            text=f"Tu pedido estará listo en ➡️ " f"{minutos:02}:{segundos:02}")
                crono_segundos -= 1
                ventana.after(1000, crono_pedido)
            else:
                cronometro_pedido.config(text="Ya podés retirar tu pedido!",font="Helvetica 20 bold")
                crono_segundos=5
        # Muestra el cronómetro
        cronometro_pedido = tk.Label(ventana_p, font=('Helvetica', 20), bg='#f4f4f4', fg='#333')
        cronometro_pedido.pack(side='top', padx=25, pady=25)

        def lista_compra():
            for elemento in ventana_carrito.get(0,tk.END):
                lista_pedidos_hechos.insert(tk.END,elemento)   

        def cerrar_ventana_ped():
            ventana_p.withdraw()
            main()
            combobox.set("")
            ventana_carrito.delete(0,tk.END)
            ocultar_adicionales()

        
        
        
        marco_2= tk.Frame(ventana_p, bg='#e0e0e0', relief=tk.RAISED, borderwidth=1)
        marco_2.place(x=20, y=110, width=470, height=170)

        marco_listbox_2=tk.Frame(marco_2)
        marco_listbox_2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        lista_pedidos_hechos = tk.Listbox(marco_listbox_2,font=('Helvetica', 14), 
                                        bg='#ffffff', fg='#333',
                                        height=8, selectbackground='#ccc',
                                        activestyle=tk.NONE)
        lista_pedidos_hechos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ###Scrollbar Vertical
        scrollbar_v2 = tk.Scrollbar(marco_listbox_2,orient="vertical")
        scrollbar_v2.pack(side=tk.RIGHT, fill=tk.Y) 
        
        lista_pedidos_hechos.config(yscrollcommand=scrollbar_v2.set)
        scrollbar_v2.config(command=lista_pedidos_hechos.yview)

        ###Scrollbar Horizontal
        scrollbar_h2 = tk.Scrollbar(lista_pedidos_hechos,orient='horizontal')    
        scrollbar_h2.pack(side=tk.BOTTOM, fill=tk.X)

        lista_pedidos_hechos.config(xscrollcommand=scrollbar_h2.set)
        scrollbar_h2.config(command=lista_pedidos_hechos.xview)
    

        ####    Botones
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

        crono_pedido()
        lista_compra()
        

        ventana_p.mainloop()

    # Funciones para mostrar y ocultar la sección de adicionales
    def mostrar_adicionales():
        #carrito_nom_adicionales.place(x=20, y=110)
        combobox.place(x=20, y=50)
        boton_agregar.place(x=20, y=80, width=130, height=30)
        #label_mensaje_adicionales.place(x=20, y=20)

    def ocultar_adicionales():
        #carrito_nom_adicionales.place_forget()
        combobox.place_forget()
        boton_agregar.place_forget()
        label_mensaje_adicionales.config(text="⬆️Seleccioná un producto del menú",
                                        font=("Helvetica", 14,"bold"))
        label_mensaje_adicionales.place(x=10, y=20)  # Muestra el mensaje cuando no hay productos

    # Función para actualizar el mensaje de adicionales según el producto
    def actualizar_mensaje_adicionales(producto):
        mensaje = "¿Le querés agregar un adicional?"
        label_mensaje_adicionales.config(text=mensaje)

    ####    Main Menu    ####
    barra_menu = tk.Menu(ventana, bg="#2e2e2e", fg="white")
    ventana.config(menu=barra_menu)
    menu_principal = tk.Menu(barra_menu, bg="#2e2e2e", fg="white", tearoff=0)
    barra_menu.add_cascade(label='Menú',menu=menu_principal)

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


    ####    Reloj    ####
    reloj = tk.Label(ventana, font=('Helvetica', 20), bg='#f4f4f4', fg='#333')
    reloj.pack(anchor='ne', padx=5, pady=5)
    hora()

    # Scrollable Cart   
    carrito_nom = tk.Label(ventana, text="Carrito:", font=('Helvetica', 14), bg='#f4f4f4', fg='#333')
    carrito_nom.place(x=20, y=135)

    ####    Adicionales    ####
    opciones = ["+Cheddar", "+Panceta", "+Cebolla", "+Tomate", "+Lechuga"]
    combobox = ttk.Combobox(ventana, values=opciones, font=('Helvetica', 12))

    # carrito_nom_adicionales = tk.Label(ventana, text="Adicionales", 
    #                                    font=('Helvetica', 14), bg='#f4f4f4', 
    #                                    fg='#333')

    # Label para el mensaje dinámico
    label_mensaje_adicionales = tk.Label(ventana, text="⬆️Seleccioná un producto del menú", 
                                        font=("Helvetica", 14,"bold"), bg='#f4f4f4', fg='#333')

    # Crear el marco
    marco = tk.Frame(ventana, bg='#e0e0e0', relief=tk.RAISED, borderwidth=1)
    marco.place(x=20, y=160, width=550, height=200)

    marco_listbox = tk.Frame(marco)
    marco_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Crear el Listbox
    ventana_carrito = tk.Listbox(marco_listbox, font=('Helvetica', 14), bg='#ffffff', fg='#333',
                                height=8, selectbackground='#ccc', activestyle=tk.NONE)
    ventana_carrito.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar Vertical
    scrollbar_vertical = tk.Scrollbar(marco_listbox, orient="vertical")
    scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

    ventana_carrito.config(yscrollcommand=scrollbar_vertical.set)
    scrollbar_vertical.config(command=ventana_carrito.yview)

    # Scrollbar Horizontal
    scrollbar_horizontal = tk.Scrollbar(marco, orient="horizontal")
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

    ventana_carrito.config(xscrollcommand=scrollbar_horizontal.set)
    scrollbar_horizontal.config(command=ventana_carrito.xview)

    ####    BOTONES    ####
    boton_agregar = tk.Button(ventana, text="Agregar adicional",
                            font=('Helvetica', 12), 
                            bg='#4CAF50', fg='white', 
                            relief=tk.RAISED, borderwidth=1,
                            command=agregar_adicional)

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

    # Ocultar los elementos adicionales al iniciar la ventana
    ocultar_adicionales()

    ####    Loop principal
    ventana.mainloop()


if __name__==__name__:
    main()