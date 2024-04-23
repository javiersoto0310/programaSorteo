from participante import Participante
from premio import Premio
import random
import os


class Sorteo:
    def __init__(self):
        self.participante = Participante()
        self.premio = Premio()
        self.participante.ingresar_participante()
        self.premio.ingresar_cantidad_de_premios()
        self.cantidad_de_participantes = self.participante.lista_de_participantes
        self.premio = self.premio.cantidad_de_premios

    def realizar_sorteo(self):
        os.system("cls")
        print("---------------------------------------------")
        print("           Lista de participantes")
        print("---------------------------------------------")
        for participante in self.cantidad_de_participantes:
            print(participante)

        while True:
            os.system("cls")
            print("""-------------------------------------------
                SORTEAR!!!!
1 - Realizar sorteo.
2 - Borrar datos.
-------------------------------------------""")
            try:     
                opcion = int(input("Ingrese una opción: "))
                if opcion == 1:
                    while self.premio >= len(self.cantidad_de_participantes):
                        os.system("cls")
                        print("Los premios no pueden superar o igualar a la cantidad de participantes!!!!")
                        print(f"Cantidad de participantes anotados: {len(self.cantidad_de_participantes)}")
                        print(f"Cantidad de premios: {self.premio}")
                        print("---------------------------------------------")
                        print("Vuelva a ingresar la cantidad de premios.")
                        self.participante = Participante()
                        self.premio = Premio()
                        self.premio.ingresar_cantidad_de_premios()
                        self.premio = self.premio.cantidad_de_premios
                    else:    
                        nombres_participantes = random.sample(self.cantidad_de_participantes, self.premio)
                        os.system("cls")
                        print("--------------------------------------------------------")
                        print("Ganador o ganadores del sorteo!!!!!")
                        print("--------------------------------------------------------")
                        for i ,participante in enumerate(nombres_participantes): 
                            print(f"Puesto número {i + 1}: {participante}")
                        break
                elif opcion == 2:
                    os.system("cls")
                    self.participante = Participante()
                    self.premio = Premio()
                    self.participante.ingresar_participante()
                    self.premio.ingresar_cantidad_de_premios()
                    self.cantidad_de_participantes = self.participante.lista_de_participantes
                    self.premio = self.premio.cantidad_de_premios
                    
                else:
                    print("Debe ingresar una opción válida.") 
            except ValueError: 
                print("Opción inválida.")                   
            
sorteo = Sorteo()
sorteo.realizar_sorteo()        













