from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.usuarios as usr
from frmeditproducto import Editor
import bll.administracion as adm


#ventana tkinter y POO

class Modificar_producto(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.select_cod = -1
       
        #setting title
        self.title("Modificar Producto")
        #setting window size 
        #TO DO : AGRANDAR VENTANA PARA QUE ENTRE LA BUSQUEDA DEL PRODUCTO
        #TO DO: AGREGAR UNA SCROLL PARA LA BUSQUEDA
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_518=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_518["font"] = ft
        GLabel_518["fg"] = "#333333"
        GLabel_518["justify"] = "center"
        GLabel_518["text"] = "Modificar Producto"
        GLabel_518.place(x=130,y=10,width=182,height=30)

        GLabel_196=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_196["font"] = ft
        GLabel_196["fg"] = "#333333"
        GLabel_196["justify"] = "center"
        GLabel_196["text"] = "Nombre Producto"
        GLabel_196.place(x=30,y=50,width=110,height=30)

        GLineEdit_94=tk.Entry(self,name="txtProdBuscar")
        GLineEdit_94["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_94["font"] = ft
        GLineEdit_94["fg"] = "#333333"
        GLineEdit_94["justify"] = "left"
        GLineEdit_94["text"] = ""
        GLineEdit_94.place(x=150,y=50,width=222,height=30)


        GButton_747=tk.Button(self)
        GButton_747["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_747["font"] = ft
        GButton_747["fg"] = "#000000"
        GButton_747["justify"] = "center"
        GButton_747["text"] = "Buscar"
        GButton_747.place(x=380,y=50,width=70,height=25)
        GButton_747["command"] = self.GButton_747_command

        GButton_534=tk.Button(self)
        GButton_534["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_534["font"] = ft
        GButton_534["fg"] = "#000000"
        GButton_534["justify"] = "center"
        GButton_534["text"] = "Modificar"
        GButton_534.place(x=110,y=250,width=70,height=25)
        GButton_534["command"] = self.GButton_534_command

        GButton_674=tk.Button(self)
        GButton_674["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_674["font"] = ft
        GButton_674["fg"] = "#000000"
        GButton_674["justify"] = "center"
        GButton_674["text"] = "Salir"
        GButton_674.place(x=220,y=250,width=70,height=25)
        GButton_674["command"] = self.GButton_674_command

        tv = ttk.Treeview(self, columns=("id", "marca", "stock", "precio","categoria"), name="tvProductos")
        tv.column("#0", width=50)
        tv.column("id", width=250, anchor=CENTER)
        tv.column("marca", width=70, anchor=CENTER)
        tv.column("stock", width=50, anchor=CENTER)
        tv.column("precio", width=50, anchor=CENTER)
        tv.column("categoria", width=100, anchor=CENTER)

        tv.heading("#0", text="Codigo", anchor=CENTER)
        tv.heading("id", text="Nombre Producto", anchor=CENTER)
        tv.heading("marca", text="Marca", anchor=CENTER)
        tv.heading("stock", text="Stock", anchor=CENTER)
        tv.heading("precio", text="Precio", anchor=CENTER)
        tv.heading("categoria", text="Categoria", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=30,y=110,width=600,height=106)    

        cantidad_productos = dict(usr.listar_stock(self.select_cod))
        cb_cantidad_productos = ttk.Combobox(self, state="readonly", values=list(cantidad_productos.values()), name="cbCantidadProductos")
        cb_cantidad_productos.current(0)
        cb_cantidad_productos.place(x=190,y=260,width=206,height=30)

    def get_value(self, name):
            return self.nametowidget(name).get()
    
    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_cod = int(data["text"])
        else:
            self.select_cod = -1
            
    #acciones del boton 'buscar'
    def GButton_747_command(self):
        producto_buscado = self.get_value("txtProdBuscar")
        tvProductos =self.nametowidget("tvProductos")
        for record in tvProductos.get_children():
            tvProductos.delete(record)
        productos = adm.listar_productos(producto_buscado)
        if len(productos)>0:
            for producto in productos:
                tvProductos.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4], producto[6]))     
        else:
            tkMsgBox.showwarning(self.master.title(), "Ningun producto encontrado")

    #boton modificar
    def GButton_534_command(self):
        producto=adm.obtener_producto(self.select_cod)
        Editor(producto,self)


    #boton salir
    def GButton_674_command(self):
        self.destroy()

