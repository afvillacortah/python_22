from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.categoria_productos as cat
import bll.productos as pro
import bll.usuarios as usr


class DashboardUser(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.select_cod = -1
        self.stock = -1
        self.cant_articulos = 0
        self.cantidad_elim = -1
        self.current_user = self.master.user_name
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
        GButton_590.place(x=290,y=440,width=117,height=30) 
        GButton_590["command"] = self.GButton_590_command

        tvCarrito = ttk.Treeview(self, columns=("id", "marca", "cantidad", "precio","categoria"), name="tvCarrito")
        tvCarrito.column("#0", width=50)
        tvCarrito.column("id", width=250, anchor=CENTER)
        tvCarrito.column("marca", width=70, anchor=CENTER)
        tvCarrito.column("cantidad", width=50, anchor=CENTER)
        tvCarrito.column("precio", width=50, anchor=CENTER)
        tvCarrito.column("categoria", width=100, anchor=CENTER)

        tvCarrito.heading("#0", text="Codigo", anchor=CENTER)
        tvCarrito.heading("id", text="Nombre Producto", anchor=CENTER)
        tvCarrito.heading("marca", text="Marca", anchor=CENTER)
        tvCarrito.heading("cantidad", text="Cantidad", anchor=CENTER)
        tvCarrito.heading("precio", text="Precio", anchor=CENTER)
        tvCarrito.heading("categoria", text="Categoria", anchor=CENTER)
        tvCarrito.bind("<<TreeviewSelect>>", self.obtener_fila_carrito)
        tvCarrito.place(x=70,y=280,width=600,height=106)

        GButton_947=tk.Button(self)
        GButton_947["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_947["font"] = ft
        GButton_947["fg"] = "#000000"
        GButton_947["justify"] = "center"
        GButton_947["text"] = "Confirmar Compra"
        GButton_947.place(x=120,y=440,width=120,height=31)
        GButton_947["command"] = self.GButton_947_command

        GButton_415=tk.Button(self)
        GButton_415["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_415["font"] = ft
        GButton_415["fg"] = "#000000"
        GButton_415["justify"] = "center"
        GButton_415["text"] = "Eliminar Producto"
        GButton_415.place(x=390,y=230,width=111,height=30)
        GButton_415["command"] = self.GButton_415_command

    def obtener_lista_carrito(self):
        lista = []
        tvCarro = self.nametowidget('tvCarrito')
        for child in tvCarro.get_children():
            dato = tvCarro.item(child)
            lista.append((dato['text'],dato['values'][0],dato['values'][1],dato['values'][2],float(dato['values'][3])))
        return lista
        
       

    #boton CONFIRMAR COMPRA
    def GButton_947_command(self):
        #obtener una lista de listas [cod.,cant.comprar,precio_articulo]
        lista_compra =self.obtener_lista_carrito()
        #valida cada producto si esta los compra
        usr.valida_lista_productos(lista_compra) 
        #cargar la compra en la tablas de detalles_pedidos y pedidos 
        ticket =[]
        if(len(lista_compra) > 0):
            user = self.current_user
            ticket = usr.registrar_compra(lista_compra,user)  
            tkMsgBox.showinfo(title='Compra Realizada',message=ticket) 
        else:
            tkMsgBox.showwarning(self.master.title(), "Los productos seleccionados no tienen stock disponible.") 

        

        #como obtengo cada cod prod , y cantidad  a comprar ?
        

    
  


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
    
    def obtener_fila_carrito(self,event):
        tvCarrito = self.nametowidget('tvCarrito')
        current_item = tvCarrito.focus()
        
        if current_item:
            data = tvCarrito.item(current_item)
            self.cantidad_elim =int( data['values'][2] )
            
        else:
            self.cantidad_elim = -1

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

    
    #boton agregar al carrito
    def GButton_103_command(self):
        cant_elegida = self.get_value('cbStock')
        cant_elegida = int(cant_elegida)
        cod_prod = self.select_cod
        tvCarrito = self.nametowidget('tvCarrito')
        producto = usr.obtener_datos_prod(cod_prod,cant_elegida)#valida que exista stock para agregarlo
        if(len(producto)>0):
            if (self.cant_articulos + cant_elegida <= 30 ):
                self.cant_articulos = self.cant_articulos + cant_elegida
                tvCarrito.insert("",END,text =producto[0],values=(producto[1],producto[2],cant_elegida,producto[3],producto[5]) )
            else:
                tkMsgBox.showwarning(self.master.title(), "La cantidad elegida de productos supera el limite max de 30 articulos")
        else:
            tkMsgBox.showwarning(self.master.title(), "El producto no dispone del stock necesario")
    
    #boton eliminar producto carrito
    def GButton_415_command(self):
        if(self.cantidad_elim != -1):
            tvCarrito = self.nametowidget("tvCarrito")
            item = tvCarrito.focus()
            self.cant_articulos = self.cant_articulos - self.cantidad_elim
            tvCarrito.delete(item)
        
    #boton salir
    def GButton_590_command(self):
        self.master.destroy()


if __name__ == "__main__":
    self = tk.Tk()
    app = DashboardUser(self)
    self.mainloop()
