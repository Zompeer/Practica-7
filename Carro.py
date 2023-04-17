import threading as TH
import time
import Factores as F
class Carro:
    DEAMBULANDO = 0
    BUSCANDO_LUGAR = 1
    ESTACIONANDO = 2
    DESESTACIONANDO = 3
    SALIENDO = 4
    VELOCIDAD = 0.01
    def __init__(self, carros, canvas, estacionamiento, factores):
        self.__carros = carros
        self.__canvas = canvas
        self.__factores = factores
        self.__estacionamiento = estacionamiento
        self.__x = 2
        self.__y = canvas.winfo_height()
        self.__estado = Carro.DEAMBULANDO
        self.__carro = canvas.create_rectangle(self.__x, self.__y, self.__x+28, self.__y+28, fill = "red", width=2)
        thread = TH.Thread(target = self.deambula)
        thread.daemon = True
        thread.start()
    def deambula(self):
        while(self.__estado == Carro.DEAMBULANDO):
            time.sleep(Carro.VELOCIDAD)
            self.__y -= 2
            self.__canvas.coords(self.__carro, self.__x,self.__y, self.__x+28, self.__y+28)
            if self.__y == self.__canvas.winfo_height()-126:
                if self.entrar_estacionamiento():
                    break
            if self.__y < -28:
                self.__carros.remove(self)
                del self
                break
    def entrar_estacionamiento(self):
        if self.__estacionamiento.espacio_disponible(self):
            self.__estado = Carro.BUSCANDO_LUGAR
            while(self.__estado == Carro.BUSCANDO_LUGAR):
                time.sleep(Carro.VELOCIDAD)
                self.__x+=2
                self.__canvas.coords(self.__carro, self.__x,self.__y, self.__x+28, self.__y+28)
                if self.__x == self.__estacionamiento.posicionLugar(self):
                    self.__estado = Carro.ESTACIONANDO
                    self.estacionarse()
                    break
        return False
    def estacionarse(self):
        while True:
            time.sleep(Carro.VELOCIDAD)
            self.__y+=2
            self.__canvas.coords(self.__carro, self.__x,self.__y, self.__x+28, self.__y+28)
            if self.__y == self.__canvas.winfo_height()-94:
                self.__estado = Carro.DESESTACIONANDO
                self.salir()
                break
    def salir(self):
        time.sleep(self.__factores.SALIDA)
        while self.__estado == Carro.DESESTACIONANDO:
            time.sleep(Carro.VELOCIDAD)
            self.__y-=2
            self.__canvas.coords(self.__carro, self.__x,self.__y, self.__x+28, self.__y+28)
            if self.__y == self.__canvas.winfo_height()-126:
                self.__estado = Carro.SALIENDO
                self.irse()
                break
    def irse(self):
        while self.__x < self.__canvas.winfo_width():
            time.sleep(Carro.VELOCIDAD)
            self.__x+=2
            self.__canvas.coords(self.__carro, self.__x,self.__y, self.__x+28, self.__y+28)
        self.__estacionamiento.desocupar(self)
        self.__carros.remove(self)
        del self