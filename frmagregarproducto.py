import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.administracion as adm
import bll.categoria_productos as cat

class Agregar_producto(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("Agregar Producto")
        #setting window size
        width=448
        height=405
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_2=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_2["font"] = ft
        GLabel_2["fg"] = "#333333"
        GLabel_2["justify"] = "center"
        GLabel_2["text"] = "Nombre "
        GLabel_2.place(x=30,y=50,width=70,height=25)

        GLineEdit_995=tk.Entry(self,name='txtNombre')
        GLineEdit_995["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_995["font"] = ft
        GLineEdit_995["fg"] = "#333333"
        GLineEdit_995["justify"] = "center"
        GLineEdit_995["text"] = ""
        GLineEdit_995.place(x=130,y=50,width=178,height=30)

        GLabel_518=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_518["font"] = ft
        GLabel_518["fg"] = "#333333"
        GLabel_518["justify"] = "center"
        GLabel_518["text"] = "Agregar Producto"
        GLabel_518.place(x=200,y=10,width=182,height=30)

        GLabel_245=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_245["font"] = ft
        GLabel_245["fg"] = "#333333"
        GLabel_245["justify"] = "center"
        GLabel_245["text"] = "Marca"
        GLabel_245.place(x=30,y=100,width=70,height=25)

        GLineEdit_130=tk.Entry(self,name='txtMarca')
        GLineEdit_130["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_130["font"] = ft
        GLineEdit_130["fg"] = "#333333"
        GLineEdit_130["justify"] = "center"
        GLineEdit_130["text"] = ""
        GLineEdit_130.place(x=130,y=100,width=178,height=30)

        GLabel_251=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_251["font"] = ft
        GLabel_251["fg"] = "#333333"
        GLabel_251["justify"] = "center"
        GLabel_251["text"] = "Stock"
        GLabel_251.place(x=40,y=150,width=70,height=25)

        GLineEdit_592=tk.Entry(self,name='txtStock')
        GLineEdit_592["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_592["font"] = ft
        GLineEdit_592["fg"] = "#333333"
        GLineEdit_592["justify"] = "center"
        GLineEdit_592["text"] = ""
        GLineEdit_592.place(x=130,y=150,width=180,height=30)

        GLabel_857=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_857["font"] = ft
        GLabel_857["fg"] = "#333333"
        GLabel_857["justify"] = "center"
        GLabel_857["text"] = "Precio Unitario"
        GLabel_857.place(x=30,y=200,width=100,height=25)

        GLineEdit_333=tk.Entry(self,name='txtPrecio')
        GLineEdit_333["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_333["font"] = ft
        GLineEdit_333["fg"] = "#333333"
        GLineEdit_333["justify"] = "center"
        GLineEdit_333["text"] = ""
        GLineEdit_333.place(x=130,y=200,width=181,height=30)

        GLabel_760=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_760["font"] = ft
        GLabel_760["fg"] = "#333333"
        GLabel_760["justify"] = "center"
        GLabel_760["text"] = "Categoria"
        GLabel_760.place(x=30,y=260,width=70,height=25)

        categorias_productos = dict(cat.listar())
        cb_categorias = ttk.Combobox(self, state="readonly", values=list(categorias_productos.values()), name="cbCategoria")
        cb_categorias.place(x=150,y=260,width=200,height=25)

        GButton_358=tk.Button(self)
        GButton_358["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_358["font"] = ft
        GButton_358["fg"] = "#000000"
        GButton_358["justify"] = "center"
        GButton_358["text"] = "Aceptar"
        GButton_358.place(x=100,y=320,width=70,height=25)
        GButton_358["command"] = self.GButton_358_command

        GButton_694=tk.Button(self)
        GButton_694["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_694["font"] = ft
        GButton_694["fg"] = "#000000"
        GButton_694["justify"] = "center"
        GButton_694["text"] = "Cancelar"
        GButton_694.place(x=240,y=320,width=70,height=25)
        GButton_694["command"] = self.GButton_694_command

        

    def get_value(self, name):
        return self.nametowidget(name).get()
    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_358_command(self):
        nombre_producto = self.get_value("txtNombre")
        marca = self.get_value("txtMarca")
        stock = self.get_value("txtStock")
        precio = self.get_value("txtPrecio")
        categoria = self.get_index("cbCategoria")
        
        '''
            validar que :
            el producto no exista en la base de datos,
            que el nombre sea una str != '' y str no sean solo numeros
            que la marca idem nombre
            que el stock sea un entero y  > 0
            precio  sea un numero real > 0
            categoria sea != 0 
        '''
        if (adm.valida_producto(nombre_producto,marca,stock,precio,categoria) ):
            #cargar el producto a la base de datos
            adm.agregar_producto(nombre_producto,marca,stock,precio,categoria)
            tkMsgBox.showinfo(self.master.title(), "Producto agregado exitosamente!")
            self.destroy()
        else:
            #mostrar mensaje de error segun el campo que no paso la validacion
            
            if not(adm.valida_producto_no_existe(nombre_producto,marca)):
                tkMsgBox.showwarning(self.master.title(), "El producto ya existe en nuestros registros")
            elif not(adm.valida_nom_mar(nombre_producto)):
                tkMsgBox.showwarning(self.master.title(), "Nombre del producto invalido")
            elif not(adm.valida_nom_mar(marca)):
                tkMsgBox.showwarning(self.master.title(), "Marca del producto invalido")
            elif not(adm.valida_stock(stock)):
                tkMsgBox.showwarning(self.master.title(), "Stock del producto invalido")
            elif not(adm.valida_precio(precio)):
                tkMsgBox.showwarning(self.master.title(), "Precio del producto invalido")
            elif not(adm.valida_nom_mar(categoria)):
                tkMsgBox.showwarning(self.master.title(), "Categoria del producto invalido")    
            
    def GButton_694_command(self):
        self.destroy()