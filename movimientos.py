from movimiento import Movimiento

class Movimientos:
    def __init__(self, lista):
        self.__list_mov = lista

    def __get_list_mov(self):
        return self.__list_mov

    def mostrar_movimientos(self):
        print(self.__list_mov())

    def anyadir_movimiento(self, movimiento):
        self.__get_list_mov().append(movimiento)

    def calcula_saldo(self):
        saldo = 0
        for i in self.__get_list_mov():
            saldo += i.cantidad()
        return saldo
