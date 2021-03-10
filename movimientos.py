from movimiento import Movimiento

class Movimientos:
    def __init__(self, lista):
        self.__list_mov = lista

    def __list_mov(self):
        return self.__list_mov

    def mostrar_movimientos(self):
        print(self.__list_mov())

    def anyadir_movimiento(self, movimiento):
        self.__list_mov().append(movimiento)

    def calcula_saldo(self):
        saldo = 0
        for i in self.__list_mov():
            saldo += i.cantidad()
        return saldo

m1 = Movimiento('Deposito 100', 100)
m2 = Movimiento('Retirada 50', -50)
m3 = Movimiento('Deposito 16', 16)
mov = Movimientos([m1, m2, m3])

#mov.mostrar_movimientos()

print(mov.calcula_saldo())
