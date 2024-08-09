class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def getNome(self):
        return self.nome
    
    def getNumero(self):
        return self.numero
    
    def setNome(self, nome):
        self.nome = nome
    
    def setNumero(self, numero):
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionarContato(self, nome, numero):
        contato = Contato(nome, numero)
        self.contatos.append(contato)
    
    def listarContatos(self):
        for contato in self.contatos:
            print("Nome: %s - Numero: %s" % (contato.getNome(), contato.getNumero()))
    
    def buscarContato(self, nome):
        for contato in self.contatos:
            if contato.getNome() == nome:
                return contato
        return None
    
    def removerContato(self, nome):
        contato = self.buscarContato(nome)
        if contato != None:
            self.contatos.remove(contato)
            return True
        return False
    
    def atualizarNomeContato(self, nome, novoNome):
        contato = self.buscarContato(nome)
        if contato != None:
            contato.setNome(novoNome)
            return True
        return False
    
    def atualizarNumeroContato(self, nome, novoNumero):
        contato = self.buscarContato(nome)
        if contato != None:
            contato.setNumero(novoNumero)
            return True
        return False

ag = Agenda()

ag.adicionarContato("João", "123456789")
ag.adicionarContato("Maria", "987654321")
ag.adicionarContato("Pedro", "123456789")
ag.adicionarContato("Cleber", "987654321")

print("\nLista de contatos:")
ag.listarContatos()

print("\nBuscar contato:")
print(ag.buscarContato("Maria").getNome())

print("\nRemover contato:")
if ag.removerContato("Maria"):
    print("Contato removido com sucesso")

print("\nAtualizar nome contato:")
if ag.atualizarNomeContato("João", "João da Silva"):
    print("Nome atualizado com sucesso")
    print(ag.buscarContato("João da Silva").getNome())

print("\nAtualizar numero contato:")
if ag.atualizarNumeroContato("Pedro", "987654321"):
    print("Numero atualizado com sucesso")
    print(ag.buscarContato("Pedro").getNumero())
