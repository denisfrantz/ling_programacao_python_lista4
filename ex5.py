class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pai = None
        self.mae = None
        self.filhos = []
    
    def __str__(self):
        return "Nome: %s - Idade: %s" % (self.nome, self.idade)
    
    def getPai(self):
        return self.pai
    
    def getMae(self):
        return self.mae
    
    def setPai(self, pai):
        self.pai = pai
    
    def setMae(self, mae):
        self.mae = mae
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def adicionarFilho(self, filho):
        self.filhos.append(filho)
    
    def buscarFilhos(self, nome):
        for filho in self.filhos:
            if filho.getNome() == nome:
                return filho
        return None
    
    def listarFilhos(self):
        for filho in self.filhos:
            print(filho)

mae = Pessoa("Maria", 40)
pai = Pessoa("Joao", 45)

filho1 = Pessoa("Jose", 20)
filho2 = Pessoa("Joana", 18)

mae.adicionarFilho(filho1)
mae.adicionarFilho(filho2)

pai.adicionarFilho(filho1)
pai.adicionarFilho(filho2)

filho1.setPai(pai)
filho2.setPai(pai)

filho1.setMae(mae)
filho2.setMae(mae)

print("\npessoas:")
for pessoa in [mae, pai, filho1, filho2]:
    print(pessoa)

print("\nfilhos de %s:" % mae.getNome())
mae.listarFilhos()

print("\nfilhos de %s:" % pai.getNome())
pai.listarFilhos()

print("\npai de %s:" % filho1.getNome())
print(filho1.getPai())

print("\nmae de %s:" % filho1.getNome())
print(filho1.getMae())

print("\npai de %s:" % filho2.getNome())
print(filho2.getPai())

print("\nmae de %s:" % filho2.getNome())
print(filho2.getMae())

