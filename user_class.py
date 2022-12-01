      
class usuario():
    def __init__(self,datos):
        self.__nombre = datos['nombre']
        self.__password = datos['password']
        self.__email = datos['email']
        #self.__cp= datos[cp]
        #self.__ciut = datos[cuit]
        #self.__domicilio = datos[domicilio]
        #self.__carrito = carrito()
    
    



def registrar_usuario():
    datos ={}
    datos['nombre']=input('Entre nombre: ')
    datos['password']=input('Entre password: ')
    datos['email']=input('Entre email: ')
    print(datos)

registrar_usuario()