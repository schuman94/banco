from cuenta import Cuenta
from cliente import Cliente
from movimientos import Movimientos
from movimiento import Movimiento
from cuentas import Cuentas

#Creacion de clientes
antonio = Cliente('49047421A', 'Antonio', 'Matinez')
manuel = Cliente('23423433L', 'Manuel', 'Pomarez')

#Creacion de cuentas
cuen1 = Cuenta(antonio, Movimientos([Movimiento('Deposito 100', 100), Movimiento('Retirada 50', -50), Movimiento('Deposito 16', 16)]))
cuen2 = Cuenta(antonio, Movimientos([Movimiento('Deposito 400', 400), Movimiento('Retirada 10', -10), Movimiento('Deposito 26', 26), Movimiento('Retirada 100', -100)]))
#No es necesario guardarla en una variable ya que la clase Cuentas se encarga de guardarla en una coleccion a la que podemos acceder a traves de su metodo get_cuenta
Cuenta(manuel, Movimientos([Movimiento('Deposito 11', 11), Movimiento('Retirada 20', -20), Movimiento('Deposito 36', 36)]))


print('Todas las cuentas:')
Cuentas.imprimir_cuentas()

print('Todas las cuentas de antonio:')
Cuentas.imprimir_cuentas_de(antonio)

print('La cuenta N. 3:')
print(Cuentas.get_cuenta(3))

print('Retirada de 20 en la cuenta 3:')
Cuentas.get_cuenta(3).retirar('Retirada de prueba de 20', 20)
Cuentas.imprimir_cuentas_de(manuel)

print('Mostrar historial de la cuenta 3:')
Cuentas.get_cuenta(3).mostrar_historial()
