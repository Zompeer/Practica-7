class Estacionamiento:
    def __init__(self, canvas, espacios):
        self.__espacios = [None]*12
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        canvas.create_line(32, h-128, w-32, h-128, width = 2, fill="black")
        for i in range(espacios):
            canvas.create_rectangle(32+32*i, h-64, 64+32*i, h-96, width = 2)
            canvas.create_line(32+32*i, h-96, 64+32*i, h-96, fill="white", width = 2)
    def espacio_disponible(self, carro):
        for i in range(len(self.__espacios)):
            if self.__espacios[i] == None:
                self.__espacios[i] = carro
                return True
        return False
    def posicionLugar(self, carro):
        try:
            indice = self.__espacios.index(carro)
            indice = len(self.__espacios)-(indice+1)
            return 32+32*indice+2
        except:
            print("Algo no va bien")
            return 0
    def desocupar(self, carro):
        try:
            indice = self.__espacios.index(carro)
            self.__espacios[indice] = None
        except:
            pass