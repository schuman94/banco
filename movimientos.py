import Movimiento

class Movimientos:
    def __init__(self, list_mov):
        self.__list_mov = []
        self.__set_list_mov(list_mov)

    def __list_mov(self):
        return self.__list_mov

    def __set_list_mov(self, list_mov):
        self.__list_mov + [list_mov]

    def anyadir_movimiento(self, movimiento):
        self.__list_mov.append(Movimiento(movimiento))

    def calcula_saldo(self):
        saldo = 0
        for i in self.__list_mov():
            saldo += i
        return saldo
