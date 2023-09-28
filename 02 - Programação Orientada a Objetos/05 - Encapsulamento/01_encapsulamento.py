class Conta:
    #---- Usou o underline pois é atributo PRIVATE
    def __init__(self, nro_agencia, saldo=0):
        #--- Privado
        self._saldo = saldo
        #--- Público 
        self.nro_agencia = nro_agencia



    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
