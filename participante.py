import os

class Participante:
    def __init__(self):
        self.lista_de_participantes = []

    def ingresar_participante(self):
        while True:
            try:
                print("""-----------------------------------------
            SORTEAR!!!!!!!!
-----------------------------------------
1 - Ingresar nombre del participante.
2 - Ingresar cantidad de premios.""")
                opcion = int(input("Opción: "))
                if opcion == 1:
                    nombre=input("Nombre: ").capitalize()
                    if nombre == "":
                        os.system("cls") 
                        print("Debe ingresar un nombre!!!")   
                    else:
                        os.system("cls") 
                        print("------------------------------------------")
                        print("         Lista de participantes")
                        print("------------------------------------------")
                        self.lista_de_participantes.append(nombre)
                        for participante in self.lista_de_participantes:
                            print(participante)
                elif opcion == 2:
                    break
                else:
                    print("Debe ingresar una opción válida.")  
            except ValueError:   
                os.system("cls") 
                print("----------------------------------------")
                print("            Opción inválida.")                   
           

    