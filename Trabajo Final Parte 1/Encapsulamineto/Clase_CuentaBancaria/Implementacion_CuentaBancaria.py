from Cuenta_Bancaria import Cuenta_Bancaria

cuenta_uno = Cuenta_Bancaria(10000,'Federico Ojeda')
print(cuenta_uno.consultar_saldo())
print(cuenta_uno.retirar(10000))
print(cuenta_uno.consultar_saldo())
print(cuenta_uno.retirar(0))