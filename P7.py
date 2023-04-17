import tkinter as TK
import Estacionamiento as ES
import Carro as CAR
import threading as TH
import time
import random
import Factores
import os
fact = Factores.Factores()
CLEAR = "cls"
carros = list()
def llegadaCarros(carros, canvas, estacionamiento, factores):
    while True:
        carros.append(CAR.Carro(carros, canvas, estacionamiento, factores))
        time.sleep(factores.ENTRADA)
raiz = TK.Tk()
ESPACIOS = 12
canvas = TK.Canvas(raiz, width = 64+32*ESPACIOS, height = 320)
canvas.pack()
canvas.configure(background = "white")
raiz.update()
estacionamiento = ES.Estacionamiento(canvas, ESPACIOS)

thread_llegada = TH.Thread(target = llegadaCarros, args=(carros, canvas, estacionamiento, fact))
thread_llegada.deamon = True
thread_llegada.start()
def menu():
    while True:
        os.system(CLEAR)
        print("Factor de llegada: "+str(fact.ENTRADA))
        print("Factor de salida: "+str(fact.SALIDA))
        print("1) Modificar factor de entrada")
        print("2) Modificar factor de salida")
        opc = input("Opcion: ")
        if opc == "1":
            try:
                can = float(input("Nuevo factor: "))
                if can>0:
                    fact.ENTRADA = can
                else:
                    raise Exception("Solo valores mayor que 0")
            except:
                continue
        elif opc=="2":
            try:
                can = float(input("Nuevo factor: "))
                if can>0:
                    fact.SALIDA = can
                else:
                    raise Exception("Solo valores mayor que 0")
            except:
                continue
menu_thread = TH.Thread(target = menu)
menu_thread.deamon = True
menu_thread.start()
raiz.mainloop()