class Movimiento:
    def __init__(self, concepto, cantidad):
        self.__concepto = concepto
        self.__cantidad = cantidad

    def concepto(self):
        return self.concepto

    def cantidad(self):
        return self.cantidad
