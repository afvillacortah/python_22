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
        GButton_670["text"] = "Entrar"
        GButton_670.place(x=210,y=180,width=171,height=30)
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

    def GButton_670_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
