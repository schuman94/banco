class Movimiento:
    def __init__(self, concepto, cantidad):
        self.__set_concepto(concepto)
        self.__set_cantidad(cantidad)

    def __set_concepto(self, concepto):
        self.__concepto = concepto

    def __set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def concepto(self):
        return self.__concepto

    def cantidad(self):
        return self.__cantidad

    def __str__(self):
        return 'Cantidad: ' + str(self.cantidad()) + ' | Concepto: ' + str(self.concepto())
