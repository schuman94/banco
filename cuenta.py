import Cliente
import Movimientos
import Movimiento

class Cuenta:
    def __init__(self, numero, titular, movimientos):
        self.__set_numero(numero)
        self.set_titular(titular)
        self.set_movimientos(movimientos)
        self.__actualizar_saldo()

    def __set_numero(self, numero):
        self.__numero = numero

    def set_titular(self, titular):
        self.__titular = Cliente(titular)

    def __set_movimientos(self, movimientos):
        self.__movimientos = Movimientos(movimientos)

    def __actualizar_saldo(self, cantidad):
            self.__saldo = self.__movimientos.calcula_saldo()

    def saldo_actual(self):
        return self.__saldo

#Utilizar funciones de orden superior para unificar retirar y depositar
    def retirar(self, concepto, cantidad):
        m = Movimiento(concepto, -cantidad)
        self.__movimientos.anyadir_movimientos(m)
        self.actualizar_saldo(cantidad)

    def depositar(self, concepto, cantidad):
        m = Movimiento(concepto, cantidad)
        self.__movimientos.anyadir_movimientos(m)
        self.actualizar_saldo(cantidad)
