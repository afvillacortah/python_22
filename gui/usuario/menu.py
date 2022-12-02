import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_344=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_344["font"] = ft
        GLabel_344["fg"] = "#333333"
        GLabel_344["justify"] = "center"
        GLabel_344["text"] = "Supermark"
        GLabel_344.place(x=200,y=20,width=197,height=30)

        GButton_51=tk.Button(root)
        GButton_51["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_51["font"] = ft
        GButton_51["fg"] = "#000000"
        GButton_51["justify"] = "center"
        GButton_51["text"] = "Registro"
        GButton_51.place(x=220,y=70,width=167,height=30)
        GButton_51["command"] = self.GButton_51_command

        GButton_71=tk.Button(root)
        GButton_71["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "Iniciar Sesion"
        GButton_71.place(x=220,y=120,width=168,height=30)
        GButton_71["command"] = self.GButton_71_command

        GButton_73=tk.Button(root)
        GButton_73["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#000000"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "Seleccionar Productos"
        GButton_73.place(x=220,y=170,width=167,height=30)
        GButton_73["command"] = self.GButton_73_command

        GButton_123=tk.Button(root)
        GButton_123["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_123["font"] = ft
        GButton_123["fg"] = "#000000"
        GButton_123["justify"] = "center"
        GButton_123["text"] = "Ver productos seleccionados"
        GButton_123.place(x=220,y=220,width=172,height=30)
        GButton_123["command"] = self.GButton_123_command

        GButton_670=tk.Button(root)
        GButton_670["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_670["font"] = ft
        GButton_670["fg"] = "#000000"
        GButton_670["justify"] = "center"
        GButton_670["text"] = "Autorizar Compra"
        GButton_670.place(x=220,y=270,width=171,height=30)
        GButton_670["command"] = self.GButton_670_command

    def GButton_51_command(self):
        print("command")


    def GButton_71_command(self):
        print("command")


    def GButton_73_command(self):
        print("command")


    def GButton_123_command(self):
        print("command")


    def GButton_670_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
