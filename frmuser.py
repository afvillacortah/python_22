from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol

class User(Toplevel):
    def __init__(self, master=None, isAdmin = False, user_id = None):        
        super().__init__(master)
        self.master = master
        self.user_id = user_id       
        self.title("Registro de cuenta")        
        width=679
        height=509
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_243 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Usuario:"
        GLabel_243.place(x=60,y=40,width=70,height=25)

        GLineEdit_871 = Entry(self, name="txtUsuario")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=170,y=40,width=211,height=30)

        GLabel_599 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Contraseña:"
        GLabel_599.place(x=60,y=80,width=70,height=25)

        GLineEdit_911 = Entry(self, show="*",name="txtContraseña")
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=170,y=80,width=210,height=30)        

        GLabel_600 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["justify"] = "center"
        GLabel_600["height"] = 30
        GLabel_600["text"] = "Confirme\nContraseña:"
        GLabel_600.place(x=60,y=120,width=102,height=30)

        GLineEdit_208 = Entry(self,show="*",  name="txtConfirmacion")
        GLineEdit_208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_208["font"] = ft
        GLineEdit_208["fg"] = "#333333"
        GLineEdit_208["justify"] = "left"
        GLineEdit_208["text"] = ""
        GLineEdit_208.place(x=170,y=120,width=209,height=30)

        GLabel_737 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "Nombre:"
        GLabel_737.place(x=60,y=170,width=70,height=25)

        GLineEdit_234 = Entry(self, name="txtNombre")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=170,y=160,width=207,height=30)

        GLabel_454 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_454["font"] = ft
        GLabel_454["fg"] = "#333333"
        GLabel_454["anchor"] = "e"
        GLabel_454["text"] = "Apellido:"
        GLabel_454.place(x=60,y=200,width=70,height=25)

        GLineEdit_384 = Entry(self, name="txtApellido")
        GLineEdit_384["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_384["font"] = ft
        GLineEdit_384["fg"] = "#333333"
        GLineEdit_384["justify"] = "left"
        GLineEdit_384["text"] = ""
        GLineEdit_384.place(x=170,y=200,width=206,height=30)

        GLabel_616 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#333333"
        GLabel_616["anchor"] = "e"
        GLabel_616["text"] = "DNI:"
        GLabel_616.place(x=60,y=240,width=70,height=25)

        GLineEdit_481 = Entry(self, name="txtDni")
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "left"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=170,y=240,width=206,height=30)

        GLabel_61 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["anchor"] = "e"
        GLabel_61["text"] = "Email:"
        GLabel_61.place(x=60,y=280,width=70,height=25)

        GLineEdit_366 = Entry(self,name="txtEmail")
        GLineEdit_366["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_366["font"] = ft
        GLineEdit_366["fg"] = "#333333"
        GLineEdit_366["justify"] = "left"
        GLineEdit_366["text"] = ""
        GLineEdit_366.place(x=170,y=280,width=207,height=30)        

        GLabel_524 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#333333"
        GLabel_524["anchor"] = "e"
        GLabel_524["text"] = "Domicilio:"
        GLabel_524.place(x=60,y=320,width=70,height=25)

        GLineEdit_126 = Entry(self,name="txtDomicilio")
        GLineEdit_126["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_126["font"] = ft
        GLineEdit_126["fg"] = "#333333"
        GLineEdit_126["justify"] = "left"
        GLineEdit_126["text"] = ""
        GLineEdit_126.place(x=170,y=320,width=208,height=30)        


        GLabel_761=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_761["font"] = ft
        GLabel_761["fg"] = "#333333"
        GLabel_761["justify"] = "center"
        GLabel_761["text"] = "Ciudad"
        GLabel_761.place(x=60,y=360,width=70,height=25)

        GLineEdit_902=Entry(self,name='txtCiudad')
        GLineEdit_902["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_902["font"] = ft
        GLineEdit_902["fg"] = "#333333"
        GLineEdit_902["justify"] = "center"
        GLineEdit_902["text"] = ""
        GLineEdit_902.place(x=170,y=360,width=207,height=30)

        GLabel_566=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_566["font"] = ft
        GLabel_566["fg"] = "#333333"
        GLabel_566["justify"] = "center"
        GLabel_566["text"] = "Telefono"
        GLabel_566.place(x=60,y=400,width=70,height=25)

        GLineEdit_861=Entry(self,name='txtTelefono')
        GLineEdit_861["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_861["font"] = ft
        GLineEdit_861["fg"] = "#333333"
        GLineEdit_861["justify"] = "center"
        GLineEdit_861["text"] = ""
        GLineEdit_861.place(x=170,y=400,width=206,height=30)

        GLabel_975 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#333333"
        GLabel_975["anchor"] = "e"
        GLabel_975["text"] = "Rol:"
        GLabel_975.place(x=60,y=450,width=70,height=25)
        
        roles = dict(rol.listar())
       
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[2])
        cb_roles.place(x=170,y=450,width=80,height=25)

        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=290,y=450,width=83,height=30)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=410,y=450,width=76,height=30)
        GButton_341["command"] = self.GButton_341_command

        if user_id is not None:
            usuario = user.obtener_id(user_id)
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                # TODO bloquear el campo usuario
                GLineEdit_871.insert(0, usuario[1])
                GLineEdit_911.insert(0, usuario[2])
                GLineEdit_208.insert(0, usuario[3]) # TODO corregir formato de fecha
                GLineEdit_234.insert(0, usuario[4])
                GLineEdit_384.insert(0, usuario[5])
                GLineEdit_481.insert(0, usuario[6])                
                cb_roles.set(usuario[8])

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        try:
            usuario = self.get_value("txtUsuario")
            contrasenia = self.get_value("txtContraseña")            
            confirmacion = self.get_value("txtConfirmacion")            
            nombre = self.get_value("txtNombre")            
            apellido = self.get_value("txtApellido")
            dni = self.get_value("txtDni")            
            email = self.get_value("txtEmail")
            domicilio = self.get_value("txtDomicilio")
            ciudad = self.get_value("txtCiudad")
            telefono = self.get_value("txtTelefono")            
            

            
            rol_id = self.get_index("cbRoles")

            
            if self.user_id is None:
                print("Alta de usuario")
                if ( user.valida_datos_registro(usuario,contrasenia,confirmacion,nombre,apellido,dni,email,domicilio,ciudad,telefono) ) :
                    user.agregar_usuario(usuario,contrasenia,nombre,apellido,dni,email,domicilio,ciudad,telefono, rol_id)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    if user.existe_usuario(usuario):
                        tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")
                    elif not(user.password_iguales(contrasenia,confirmacion)):
                        tkMsgBox.showwarning(self.master.title(), "La contraseña no coincide con la confirmacion")
                    elif not(user.es_text_sin_espacios(usuario)):
                        tkMsgBox.showwarning(self.master.title(), "Formato de Usuario invalido")
                    elif not(user.es_text_sin_espacios(contrasenia)):
                        tkMsgBox.showwarning(self.master.title(), "Formato de Contraseña invalido")
                    elif not(user.valida_nombre_ape(nombre)):
                        tkMsgBox.showwarning(self.master.title(), "Formato de Nombre invalido")
                    elif not(user.valida_nombre_ape(apellido)):
                        tkMsgBox.showwarning(self.master.title(), "Formato de Apellido invalido")
                    elif not(user.es_numero(dni)):
                        tkMsgBox.showwarning(self.master.title(), "Formato DNI invalido, debe contener solo digitos")
                    elif not(user.es_numero(telefono)):
                        tkMsgBox.showwarning(self.master.title(), "Formato de Telefono invalido, debe contener solo digitos")
                    elif not (user.valida_ciudad(ciudad)):
                        tkMsgBox.showwarning(self.master.title(),"Formato de Ciudad invalida")                        
                    else:
                        tkMsgBox.showwarning(self.master.title(), "Formato de Email invalido!")
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id, apellido, nombre,  dni, email, contrasenia, rol_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))