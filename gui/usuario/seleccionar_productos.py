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

        GButton_670=tk.Button(root)
        GButton_670["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_670["font"] = ft
        GButton_670["fg"] = "#000000"
        GButton_670["justify"] = "center"
        GButton_670["text"] = "Agregar"
        GButton_670.place(x=330,y=330,width=171,height=30)
        GButton_670["command"] = self.GButton_670_command

        GLabel_369=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_369["font"] = ft
        GLabel_369["fg"] = "#333333"
        GLabel_369["justify"] = "center"
        GLabel_369["text"] = "Producto"
        GLabel_369.place(x=70,y=60,width=141,height=30)

        GLineEdit_439=tk.Entry(root)
        GLineEdit_439["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_439["font"] = ft
        GLineEdit_439["fg"] = "#333333"
        GLineEdit_439["justify"] = "center"
        GLineEdit_439["text"] = ""
        GLineEdit_439.place(x=210,y=60,width=228,height=30)

        GButton_115=tk.Button(root)
        GButton_115["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_115["font"] = ft
        GButton_115["fg"] = "#000000"
        GButton_115["justify"] = "center"
        GButton_115["text"] = "Buscar"
        GButton_115.place(x=500,y=60,width=70,height=25)
        GButton_115["command"] = self.GButton_115_command

        GMessage_635=tk.Message(root)
        GMessage_635["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_635["font"] = ft
        GMessage_635["fg"] = "#333333"
        GMessage_635["justify"] = "center"
        GMessage_635["text"] = ""
        GMessage_635.place(x=150,y=110,width=352,height=168)

        GLineEdit_50=tk.Entry(root)
        GLineEdit_50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_50["font"] = ft
        GLineEdit_50["fg"] = "#333333"
        GLineEdit_50["justify"] = "center"
        GLineEdit_50["text"] = ""
        GLineEdit_50.place(x=200,y=310,width=70,height=25)

        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "Cantidad"
        GLabel_819.place(x=90,y=350,width=70,height=25)

        GLabel_202=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_202["font"] = ft
        GLabel_202["fg"] = "#333333"
        GLabel_202["justify"] = "center"
        GLabel_202["text"] = "Cod, Prod"
        GLabel_202.place(x=90,y=310,width=70,height=25)

        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "#333333"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["text"] = ""
        GLineEdit_334.place(x=200,y=350,width=70,height=25)

        GMessage_532=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_532["font"] = ft
        GMessage_532["fg"] = "#333333"
        GMessage_532["justify"] = "center"
        GMessage_532["text"] = ""
        GMessage_532.place(x=180,y=400,width=291,height=30)

    def GButton_670_command(self):
        print("command")


    def GButton_115_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
