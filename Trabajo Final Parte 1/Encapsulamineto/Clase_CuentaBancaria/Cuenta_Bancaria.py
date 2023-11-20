class Cuenta_Bancaria():
    
    def __init__(self,saldo,titular):
        self.__saldo = saldo
        self.titular = titular
    
    def depositar(self,deposito):
        if deposito < 1:
            return f'No se puede depositar la catidad de dinero, ya que el valor ingresado no supera el mínimo de depósito.'
        else:
            self._saldo = self._saldo + deposito
            return f'Se ha depositado ${deposito} en su cuenta.'
    
    def retirar(self,retiro):
        if self._saldo>0 and retiro in range(self._saldo+1):
            self._saldo = self._saldo - retiro
            return f'${retiro} retiradps exitosamente.'
        else:
            return f'No se puede retirar la catidad solicitada.'
    
    def consultar_saldo(self):
        return f'El saldo de la cuenta que corresponde a {self.titular} es de ${self._saldo}'
        
    @property
    def saldo(self):
        return self.__saldo