import tkinter as tk
import tkinter.font as tkFont
from  frmagregarproducto import  Agregar_producto
from frmmodificarproducto import Modificar_producto
from frmcomprasrealizadas import Compras
from frmuser import User
class Dashboard(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Principal Administracion")        
        width=350   
        height=307
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        
        GLabel_996=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#333333"
        GLabel_996["justify"] = "center"
        GLabel_996["text"] = "Menu Administración"
        GLabel_996.place(x=80,y=10,width=182,height=30)
        
        GButton_245=tk.Button(self)
        GButton_245["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "Cargar Producto"
        GButton_245.place(x=70,y=70,width=206,height=30)
        GButton_245["command"] = self.cargar_producto

        

        GButton_196=tk.Button(self)
        GButton_196["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_196["font"] = ft
        GButton_196["fg"] = "#000000"
        GButton_196["justify"] = "center"
        GButton_196["text"] = "Editar Producto"
        GButton_196.place(x=70,y=120,width=208,height=30)
        GButton_196["command"] = self.editar_producto

        GButton_430=tk.Button(self)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Ver Compras realizadas"
        GButton_430.place(x=70,y=170,width=205,height=30)
        GButton_430["command"] = self.compras_realizadas

        GButton_400=tk.Button(self)
        GButton_400["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_400["font"] = ft
        GButton_400["fg"] = "#000000"
        GButton_400["justify"] = "center"
        GButton_400["text"] = "Agregar Usuario"
        GButton_400.place(x=70,y=210,width=207,height=30)
        GButton_400["command"] = self.agregar_usuario

        GButton_401=tk.Button(self)
        GButton_401["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_401["font"] = ft
        GButton_401["fg"] = "#000000"
        GButton_401["justify"] = "center"
        GButton_401["text"] = "Salir"
        GButton_401.place(x=70,y=260,width=207,height=30)
        GButton_401["command"] = self.salir

        
    
    def cargar_producto(self):
        Agregar_producto(self.master)

    def editar_producto(self):
        Modificar_producto(self.master)

    def compras_realizadas(self):
        Compras(self.master)
    
    def agregar_usuario(self):
        User(self,True)
        

    def salir(self):
        self.master.destroy()
