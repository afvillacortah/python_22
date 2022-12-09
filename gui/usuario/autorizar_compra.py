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

        GMessage_635=tk.Message(root)
        GMessage_635["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_635["font"] = ft
        GMessage_635["fg"] = "#333333"
        GMessage_635["justify"] = "center"
        GMessage_635["text"] = ""
        GMessage_635.place(x=110,y=70,width=381,height=239)

        GMessage_532=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_532["font"] = ft
        GMessage_532["fg"] = "#333333"
        GMessage_532["justify"] = "center"
        GMessage_532["text"] = ""
        GMessage_532.place(x=180,y=400,width=291,height=30)

        GButton_771=tk.Button(root)
        GButton_771["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_771["font"] = ft
        GButton_771["fg"] = "#000000"
        GButton_771["justify"] = "center"
        GButton_771["text"] = "Autorizar la compra de productos"
        GButton_771.place(x=140,y=360,width=298,height=36)
        GButton_771["command"] = self.GButton_771_command

        GButton_910=tk.Button(root)
        GButton_910["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_910["font"] = ft
        GButton_910["fg"] = "#000000"
        GButton_910["justify"] = "center"
        GButton_910["text"] = "MENU"
        GButton_910.place(x=480,y=360,width=82,height=36)
        GButton_910["command"] = self.GButton_910_command

    def GButton_771_command(self):
        print("command")


    def GButton_910_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
