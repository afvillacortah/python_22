import tkinter as tk
import tkinter.font as tkFont
import bll.pedidos as ped
from tkinter import ttk
from tkinter import *
import bll.detalles_pedidos as dp
class Compras(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.select_cod=-1
        self.detalle_pedido = ""
        #setting title
        self.title("Compras Realizadas")
        #setting window size
        width=603
        height=476
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        tvPedidos = ttk.Treeview(self,columns=('fecha','usuario','monto','estado'),name='tvPedidos')
        tvPedidos.column("#0",width=50)
        tvPedidos.column("fecha",width=80,anchor=CENTER)
        tvPedidos.column("usuario",width=100,anchor=CENTER)
        tvPedidos.column("monto",width=60,anchor=CENTER)
        tvPedidos.column("estado",width=100,anchor=CENTER)
        tvPedidos.heading(column="#0",text='Codigo',anchor=CENTER)
        tvPedidos.heading(column='fecha',text='Fecha',anchor=CENTER)
        tvPedidos.heading(column='usuario',text='Usuario',anchor=CENTER)
        tvPedidos.heading(column='monto',text='Monto',anchor=CENTER)
        tvPedidos.heading(column='estado',text='Estado',anchor=CENTER)
        tvPedidos.bind("<<TreeviewSelect>>", self.obtener_cod_pedido)
        tvPedidos.place(x=60,y=30,width=480,height=179)
         
        

        GButton_569=tk.Button(self)
        GButton_569["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_569["font"] = ft
        GButton_569["fg"] = "#000000"
        GButton_569["justify"] = "center"
        GButton_569["text"] = "Marcar Entregado"
        GButton_569.place(x=250,y=230,width=126,height=30)
        GButton_569["command"] = self.GButton_569_command

        GButton_255=tk.Button(self)
        GButton_255["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_255["font"] = ft
        GButton_255["fg"] = "#000000"
        GButton_255["justify"] = "center"
        GButton_255["text"] = "Ver Detalle"
        GButton_255.place(x=380,y=230,width=147,height=30)
        GButton_255["command"] = self.GButton_255_command



        GLabel_924=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_924["font"] = ft
        GLabel_924["fg"] = "#333333"
        GLabel_924["justify"] = "center"
        GLabel_924["text"] = "Compras Realizadas"
        GLabel_924.place(x=200,y=0,width=170,height=30)

        
        
        fechas =self.obten_fechas()
        #combo box con las fechas donde elegimos que fecha queremos que se muestre

        cbFecha= ttk.Combobox(self,state="readonly",values=fechas,name="cbFecha")
        #cbFecha.current(0)
        cbFecha.bind("<<ComboboxSelected>>", self.refrescar)
        cbFecha.place(x=165,y=230,width=80,height=30)
        

        
        GLabel_633=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_633["font"] = ft
        GLabel_633["fg"] = "#333333"
        GLabel_633["justify"] = "center"
        GLabel_633["text"] = "Fecha"
        GLabel_633.place(x=30,y=230,width=113,height=30)

        GMessage_940=tk.Message(self,textvariable=self.detalle_pedido,name='msgDetalle_compra')
        ft = tkFont.Font(family='Times',size=12)
        GMessage_940["font"] = ft
        GMessage_940["fg"] = "#333333"
        GMessage_940["justify"] = "center"
        GMessage_940["anchor"]= W
        GMessage_940["text"] = ''
        GMessage_940["width"] =500
        GMessage_940.place(x=50,y=260,width=500,height=180)

    def obtener_cod_pedido(self, event):
        tvPedidos = self.nametowidget("tvPedidos")
        current_item = tvPedidos.focus()
        if current_item:
            data = tvPedidos.item(current_item)
            self.select_cod = int(data["text"])          
        else:
            self.select_cod = -1
    
   

    #al presionar el boton 'Ver Detalle' muestra en el mensaje un detalle
    def GButton_255_command(self):
        msgbox =self.nametowidget("msgDetalle_compra")

        cabecera = 'Producto \t\t\t\t Cantidad\n'
        detalle_pedido = cabecera+dp.listar_detalle(self.select_cod)
        msgbox['text']=detalle_pedido
        
        
    
    #al presionar el boton de 'marcar entregado' cambia el estado a entregado y actualiza el treeview
    def GButton_569_command(self):
        fecha =self.obten_fecha_selec()
        cod_pedido = self.select_cod
        ped.marcar_pedido_entregado(cod_pedido)
        self.refrescar('<Button-1>')
        

    def obten_fechas(self):
        return ped.listar_fechas()
    
    def obten_fecha_selec(self):
        cb = self.nametowidget("cbFecha")
        fecha = cb.get()
        return fecha
    
    def refrescar(self,event):        
        tvPedidos = self.nametowidget("tvPedidos")
        fecha_selec = self.obten_fecha_selec()
        
        for record in tvPedidos.get_children():
            tvPedidos.delete(record)

        pedidos = ped.listar_pedidos(fecha_selec)

        for pedido in pedidos:
            if(pedido[4]==0):
                tvPedidos.insert("", END, text=pedido[0], values=(pedido[1], pedido[2], pedido[3],'entregado'))
            else:
                    tvPedidos.insert("", END, text=pedido[0], values=(pedido[1], pedido[2], pedido[3],'pendiente')) 

