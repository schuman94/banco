from cuenta import Cuenta
from cliente import Cliente
from movimientos import Movimientos
from movimiento import Movimiento


antonio = Cliente('49047421A', 'Antonio', 'Matinez')
cuen1 = Cuenta(antonio, Movimientos([Movimiento('Deposito 100', 100), Movimiento('Retirada 50', -50), Movimiento('Deposito 16', 16)]))
cuen2 = Cuenta(antonio, Movimientos([Movimiento('Deposito 400', 400), Movimiento('Retirada 10', -10), Movimiento('Deposito 26', 26), Movimiento('Retirada 100', -100)]))

print(cuen1)
print(cuen2)
