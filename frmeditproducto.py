from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.administracion as adm
import bll.categoria_productos as cat
class Editor(Toplevel):
    def __init__(self, producto=(),master=None):
        super().__init__(master)
        self.master = master
        self.datos=producto
        #setting title
        self.title("Editor de Producto")
        #setting window size
        width=600
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_68=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_68["font"] = ft
        GLabel_68["fg"] = "#333333"
        GLabel_68["justify"] = "center"
        GLabel_68["text"] = "Codigo"
        GLabel_68.place(x=60,y=50,width=70,height=25)

        GMessage_740=tk.Message(self)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_740["font"] = ft
        GMessage_740["fg"] = "#333333"
        GMessage_740["justify"] = "center"
        GMessage_740["text"] = f"{producto[0]}"
        GMessage_740.place(x=190,y=50,width=205,height=31)

        GLabel_988=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_988["font"] = ft
        GLabel_988["fg"] = "#333333"
        GLabel_988["justify"] = "center"
        GLabel_988["text"] = "Nombre"
        GLabel_988.place(x=60,y=100,width=70,height=25)

        GLineEdit_244=tk.Entry(self,name='txtNombre')
        GLineEdit_244["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_244["font"] = ft
        GLineEdit_244["fg"] = "#333333"
        GLineEdit_244["justify"] = "center"
        GLineEdit_244["text"] = ""
        GLineEdit_244.insert(0,producto[1])
        GLineEdit_244.place(x=190,y=100,width=206,height=30)

        GLabel_621=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_621["font"] = ft
        GLabel_621["fg"] = "#333333"
        GLabel_621["justify"] = "center"
        GLabel_621["text"] = "Marca"
        GLabel_621.place(x=60,y=140,width=70,height=25)

        GLineEdit_978=tk.Entry(self,name='txtMarca')
        GLineEdit_978["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_978["font"] = ft
        GLineEdit_978["fg"] = "#333333"
        GLineEdit_978["justify"] = "center"
        GLineEdit_978["text"] = ''
        GLineEdit_978.insert(0,producto[2])
        GLineEdit_978.place(x=190,y=140,width=206,height=30)

        GLabel_921=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_921["font"] = ft
        GLabel_921["fg"] = "#333333"
        GLabel_921["justify"] = "center"
        GLabel_921["text"] = "Stock"
        GLabel_921.place(x=60,y=180,width=70,height=25)

        GLineEdit_70=tk.Entry(self,name='txtStock')
        GLineEdit_70["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_70["font"] = ft
        GLineEdit_70["fg"] = "#333333"
        GLineEdit_70["justify"] = "center"
        GLineEdit_70["text"] = ""
        GLineEdit_70.insert(0,producto[3])
        GLineEdit_70.place(x=190,y=180,width=207,height=30)

        GLabel_396=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_396["font"] = ft
        GLabel_396["fg"] = "#333333"
        GLabel_396["justify"] = "center"
        GLabel_396["text"] = "Precio"
        GLabel_396.place(x=60,y=220,width=70,height=25)

        GLineEdit_635=tk.Entry(self,name='txtPrecio')
        GLineEdit_635["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_635["font"] = ft
        GLineEdit_635["fg"] = "#333333"
        GLineEdit_635["justify"] = "center"
        GLineEdit_635["text"] = ""
        GLineEdit_635.insert(0,producto[4])
        GLineEdit_635.place(x=190,y=220,width=206,height=30)

        GLabel_654=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#333333"
        GLabel_654["justify"] = "center"
        GLabel_654["text"] = "Categoria"
        GLabel_654.place(x=60,y=260,width=70,height=25)

       


        categorias_productos = dict(cat.listar())
        cb_categorias = ttk.Combobox(self, state="readonly", values=list(categorias_productos.values()), name="cbCategoria")
        cb_categorias.current(producto[6]-1)
        cb_categorias.place(x=190,y=260,width=206,height=30)


        GLabel_609=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_609["font"] = ft
        GLabel_609["fg"] = "#333333"
        GLabel_609["justify"] = "center"
        GLabel_609["text"] = "Estado"
        GLabel_609.place(x=60,y=300,width=70,height=25)

        cb_estado = ttk.Combobox(self, state="readonly", values=list(('Dehabilitado','Habilitado')), name="cbEstado")
        if (producto[5] == 0):
            cb_estado.current(0)
        else:
            cb_estado.current(1)
        cb_estado.place(x=190,y=300,width=205,height=30)
        

        GButton_541=tk.Button(self)
        GButton_541["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_541["font"] = ft
        GButton_541["fg"] = "#000000"
        GButton_541["justify"] = "center"
        GButton_541["text"] = "Aceptar"
        GButton_541.place(x=130,y=330,width=70,height=25)
        GButton_541["command"] = self.GButton_541_command

        GButton_425=tk.Button(self)
        GButton_425["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_425["font"] = ft
        GButton_425["fg"] = "#000000"
        GButton_425["justify"] = "center"
        GButton_425["text"] = "Cancelar"
        GButton_425.place(x=270,y=330,width=70,height=25)
        GButton_425["command"] = self.GButton_425_command
    
    def get_value(self, name):
        return self.nametowidget(name).get()
    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_541_command(self):
        #to do : obtener campos ingresados,
        
        nombre = self.get_value('txtNombre')
        marca = self.get_value('txtMarca')
        stock = self.get_value('txtStock')
        precio = self.get_value("txtPrecio")
        estado = (self.nametowidget('cbEstado')).current()
        categoria = self.get_index("cbCategoria")

        #determinar si todos los campos son validos:
        if adm.valida_producto_actualizacion(self.datos[0],nombre,marca,stock,precio):
            adm.actualizar_producto(self.datos[0],nombre,marca,stock,precio,estado,categoria)
            tkMsgBox.showinfo(self.master.title(), "Producto modificado exitosamente!")
            self.destroy()
        else:
            if not(adm.valida_nom_mar(nombre)):
                tkMsgBox.showwarning(self.master.title(), "Nombre del producto invalido")
            elif not(adm.valida_nom_mar(marca)):
                tkMsgBox.showwarning(self.master.title(), "Marca del producto invalido")
            elif not(adm.valida_stock(stock)):
                tkMsgBox.showwarning(self.master.title(), "Stock del producto invalido")
            elif not(adm.valida_precio(precio)):
                tkMsgBox.showwarning(self.master.title(), "Precio del producto invalido") 
            print('error en campo')

        #  si : 
        #       castear los datos al tipo requerido por el campo
        #       llamar a metodo para hacer update en la bd
        # no : mostrar mensaje con error 
        pass


    def GButton_425_command(self):
        self.destroy()

