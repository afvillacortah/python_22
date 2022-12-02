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
        GButton_670["text"] = "Registar"
        GButton_670.place(x=10,y=460,width=171,height=30)
        GButton_670["command"] = self.GButton_670_command

        GLabel_369=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_369["font"] = ft
        GLabel_369["fg"] = "#333333"
        GLabel_369["justify"] = "center"
        GLabel_369["text"] = "Usuario"
        GLabel_369.place(x=70,y=60,width=141,height=30)

        GLineEdit_439=tk.Entry(root)
        GLineEdit_439["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_439["font"] = ft
        GLineEdit_439["fg"] = "#333333"
        GLineEdit_439["justify"] = "center"
        GLineEdit_439["text"] = ""
        GLineEdit_439.place(x=240,y=60,width=228,height=30)

        GLabel_937=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_937["font"] = ft
        GLabel_937["fg"] = "#333333"
        GLabel_937["justify"] = "center"
        GLabel_937["text"] = "Contraseña"
        GLabel_937.place(x=100,y=110,width=103,height=30)

        GLineEdit_572=tk.Entry(root)
        GLineEdit_572["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_572["font"] = ft
        GLineEdit_572["fg"] = "#333333"
        GLineEdit_572["justify"] = "center"
        GLineEdit_572["text"] = ""
        GLineEdit_572.place(x=240,y=110,width=227,height=30)

        GLabel_799=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_799["font"] = ft
        GLabel_799["fg"] = "#333333"
        GLabel_799["justify"] = "center"
        GLabel_799["text"] = "Email"
        GLabel_799.place(x=90,y=150,width=105,height=30)

        GLineEdit_99=tk.Entry(root)
        GLineEdit_99["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_99["font"] = ft
        GLineEdit_99["fg"] = "#333333"
        GLineEdit_99["justify"] = "center"
        GLineEdit_99["text"] = ""
        GLineEdit_99.place(x=240,y=160,width=229,height=30)

        GLabel_1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_1["font"] = ft
        GLabel_1["fg"] = "#333333"
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = "Domicilio"
        GLabel_1.place(x=90,y=210,width=96,height=30)

        GLineEdit_504=tk.Entry(root)
        GLineEdit_504["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_504["font"] = ft
        GLineEdit_504["fg"] = "#333333"
        GLineEdit_504["justify"] = "center"
        GLineEdit_504["text"] = ""
        GLineEdit_504.place(x=240,y=210,width=232,height=30)

        GLabel_393=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_393["font"] = ft
        GLabel_393["fg"] = "#333333"
        GLabel_393["justify"] = "center"
        GLabel_393["text"] = "Provincia"
        GLabel_393.place(x=100,y=270,width=70,height=25)

        GLabel_256=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Ciudad"
        GLabel_256.place(x=100,y=320,width=70,height=25)

        GLabel_909=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_909["font"] = ft
        GLabel_909["fg"] = "#333333"
        GLabel_909["justify"] = "center"
        GLabel_909["text"] = "Cod. Postal"
        GLabel_909.place(x=100,y=370,width=70,height=25)

        GLineEdit_394=tk.Entry(root)
        GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_394["font"] = ft
        GLineEdit_394["fg"] = "#333333"
        GLineEdit_394["justify"] = "center"
        GLineEdit_394["text"] = ""
        GLineEdit_394.place(x=240,y=270,width=233,height=30)

        GLineEdit_153=tk.Entry(root)
        GLineEdit_153["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_153["font"] = ft
        GLineEdit_153["fg"] = "#333333"
        GLineEdit_153["justify"] = "center"
        GLineEdit_153["text"] = ""
        GLineEdit_153.place(x=240,y=320,width=230,height=30)

        GLineEdit_881=tk.Entry(root)
        GLineEdit_881["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_881["font"] = ft
        GLineEdit_881["fg"] = "#333333"
        GLineEdit_881["justify"] = "center"
        GLineEdit_881["text"] = ""
        GLineEdit_881.place(x=240,y=370,width=232,height=30)

        GLabel_479=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_479["font"] = ft
        GLabel_479["fg"] = "#333333"
        GLabel_479["justify"] = "center"
        GLabel_479["text"] = "CUIL/CUIT"
        GLabel_479.place(x=100,y=420,width=70,height=25)

        GLineEdit_808=tk.Entry(root)
        GLineEdit_808["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_808["font"] = ft
        GLineEdit_808["fg"] = "#333333"
        GLineEdit_808["justify"] = "center"
        GLineEdit_808["text"] = ""
        GLineEdit_808.place(x=240,y=420,width=230,height=30)

    def GButton_670_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
