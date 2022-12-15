from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.categoria_productos as cat
import bll.productos as pro
import bll.usuarios as usr
import bll.administracion as adm

class Seleccionar(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.select_cod = -1
        self.stock = -1
        
        #setting title
        self.title("Seleccionar Productos")
        #setting window size
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_803=tk.Button(self)
        GButton_803["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_803["font"] = ft
        GButton_803["fg"] = "#000000"
        GButton_803["justify"] = "center"
        GButton_803["text"] = "Buscar"
        GButton_803.place(x=490,y=70,width=70,height=25)
        GButton_803["command"] = self.GButton_803_command

        GLineEdit_606=tk.Entry(self,name='txtProdBuscar')
        GLineEdit_606["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_606["font"] = ft
        GLineEdit_606["fg"] = "#333333"
        GLineEdit_606["justify"] = "center"
        GLineEdit_606["text"] = "Entry"
        GLineEdit_606.place(x=160,y=70,width=293,height=30)

        GLabel_727=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_727["font"] = ft
        GLabel_727["fg"] = "#333333"
        GLabel_727["justify"] = "center"
        GLabel_727["text"] = "Cantidad"
        GLabel_727.place(x=70,y=230,width=70,height=25)


        GLabel_618=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_618["font"] = ft
        GLabel_618["fg"] = "#333333"
        GLabel_618["justify"] = "center"
        GLabel_618["text"] = "Nombre Producto"
        GLabel_618.place(x=60,y=70,width=150,height=30)

        GButton_103=tk.Button(self)
        GButton_103["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_103["font"] = ft
        GButton_103["fg"] = "#000000"
        GButton_103["justify"] = "center"
        GButton_103["text"] = "Agregar al Carrito"
        GButton_103.place(x=220,y=230,width=120,height=30)
        GButton_103["command"] = self.GButton_103_command

        GLabel_382=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_382["font"] = ft
        GLabel_382["fg"] = "#333333"
        GLabel_382["justify"] = "center"
        GLabel_382["text"] = "Seleccionar Productos"
        GLabel_382.place(x=230,y=20,width=164,height=30)

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
        tv.place(x=70,y=120,width=600,height=106)

        

        cb_stock = ttk.Combobox(self, state="readonly", textvariable=self.stock, name="cbStock")
        cb_stock.place(x=150,y=230,width=50,height=30)
        
        GButton_590=tk.Button(self)
        GButton_590["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_590["font"] = ft
        GButton_590["fg"] = "#000000"
        GButton_590["justify"] = "center"
        GButton_590["text"] = "Salir"
        GButton_590.place(x=390,y=230,width=111,height=30)
        GButton_590["command"] = self.GButton_590_command
  


    def get_value(self, name):
            return self.nametowidget(name).get()
    
    def obtener_fila(self, event):
        tvProductos = self.nametowidget("tvProductos")
        current_item = tvProductos.focus()
        if current_item:
            data = tvProductos.item(current_item)
            self.select_cod = int(data["text"])
            self.stock = (pro.listar_stock(self.select_cod))[0]
            stockWidg = self.nametowidget('cbStock')
            lista_stock = list(range(1,self.stock+1))
            stockWidg['values']=  lista_stock
            stockWidg.current(0)
            
        else:
            self.select_cod = -1
    
    
    #acciones del boton 'buscar'
    
    def GButton_803_command(self):
        producto_buscado = self.get_value("txtProdBuscar")
        tvProductos =self.nametowidget("tvProductos")
        for record in tvProductos.get_children():
            tvProductos.delete(record)
        productos = usr.listar_productos(producto_buscado)
        if len(productos)>0:
            for producto in productos:
                tvProductos.insert("", END, text=producto[0], values=(producto[1], producto[2], producto[3], producto[4], producto[6]))     
        else:
            tkMsgBox.showwarning(self.master.title(), "Ningun producto encontrado")

    #agregar al carrito
    
    def GButton_103_command(self):
        self.master.append(1,'fideo','marolio',150,50.55,1)
        self.destroy()
    #boton salir
    def GButton_590_command(self):
        self.destroy()


if __name__ == "__main__":
    self = tk.Tk()
    app = Seleccionar(self)
    self.mainloop()
