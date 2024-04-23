import os
class Premio:
    def __init__(self):
        self.cantidad_de_premios = 0
        
    def ingresar_cantidad_de_premios(self):
        while True:
            try:
                self.cantidad_de_premios = int(input("Cantidad de premios a sortear: "))
                break
            except ValueError:
                os.system("cls") 
                print("Debe ingresar un número!!!")  
                    
