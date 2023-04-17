import random
class Factores:
    FACTORES = [0.5, 1, 2]
    def __init__(self):
        self.ENTRADA = Factores.FACTORES[random.randint(0,2)]
        self.SALIDA = Factores.FACTORES[random.randint(0,2)]