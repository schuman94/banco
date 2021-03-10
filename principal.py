from cuenta import Cuenta
from cliente import Cliente
from movimientos import Movimientos
from movimiento import Movimiento


cli = Cliente('49047421A', 'Antonio', 'Matinez')
m1 = Movimiento('Deposito 100', 100)
m2 = Movimiento('Retirada 50', -50)
m3 = Movimiento('Deposito 16', 16)
cuen = Cuenta(1, cli, Movimientos([m1, m2, m3]))

print(cuen.saldo_actual())
