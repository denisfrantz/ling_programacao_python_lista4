class Poupanca:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
    
    def getSaldo(self):
        return self.saldo

class ContaCorrente:
    def __init__(self, saldo, chequeEspecial):
        self.saldo = saldo
        self.chequeEspecial = chequeEspecial
    
    def depositarSaldo(self, valor):
        self.saldo += valor
    
    def depositarChequeEspecial(self, valor):
        self.chequeEspecial += valor
    
    def sacarSaldo(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
    
    def sacarChequeEspecial(self, valor):
        if self.chequeEspecial >= valor:
            self.chequeEspecial -= valor
            return True
        return False
    
    def getSaldo(self):
        return self.saldo
    
    def getChequeEspecial(self):
        return self.chequeEspecial
    
    def extrato(self):
        print("Saldo: %s - Cheque Especial: %s" % (self.saldo, self.chequeEspecial))

class Banco:
    def __init__(self):
        self.contas = []
        self.poupancas = []
    
    def abreConta(self):
        conta = ContaCorrente(0, 0)
        self.contas.append(conta)
    
    def abrePoupanca(self):
        poupanca = Poupanca(0)
        self.poupancas.append(poupanca)
    
    def depositarSaldo(self, conta, valor):
        conta.depositarSaldo(valor)
    
    def depositarChequeEspecial(self, conta, valor):
        conta.depositarChequeEspecial(valor)
    
    def depositarPoupanca(self, poupanca, valor):
        poupanca.depositar(valor)
    
    def sacarSaldo(self, conta, valor):
        conta.sacarSaldo(valor)
    
    def sacarChequeEspecial(self, conta, valor):
        conta.sacarChequeEspecial(valor)
    
    def sacarPoupanca(self, poupanca, valor):
        poupanca.sacar(valor)
    
    def extrato(self, conta):
        conta.extrato()
    
    def extratoTotal(self):
        for conta in self.contas:
            conta.extrato()
        for poupanca in self.poupancas:
            print("Poupanca: %s" % poupanca.getSaldo())

banco = Banco()

banco.abreConta()
banco.contas[0].depositarSaldo(1000)

banco.abrePoupanca()
banco.poupancas[0].depositar(1000)

banco.extratoTotal()