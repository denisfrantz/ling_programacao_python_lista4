class CadastroEmpregado:
    def __init__(self, nome, idade, funcao, nascimento, telefone, peso, altura, salario):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.nascimento = nascimento
        self.telefone = telefone
        self.peso = peso
        self.altura = altura
        self.salario = salario
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def setFuncao(self, funcao):
        self.funcao = funcao
    
    def setNascimento(self, nascimento):
        self.nascimento = nascimento
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def setPeso(self, peso):
        self.peso = peso
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setSalario(self, salario):
        self.salario = salario
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def getFuncao(self):
        return self.funcao
    
    def getNascimento(self):
        return self.nascimento
    
    def getTelefone(self):
        return self.telefone
    
    def getPeso(self):
        return self.peso
    
    def getAltura(self):
        return self.altura
    
    def getSalario(self):
        return self.salario

funcionario = CadastroEmpregado("João", 25, "Programador", "01/01/2000", "123456789", 80, 1.70, 2000)

print("Nome: ", funcionario.getNome())
print("Idade: ", funcionario.getIdade())
print("Função na empresa: ", funcionario.getFuncao())
print("Data de nascimento: ", funcionario.getNascimento())
print("Telefone: ", funcionario.getTelefone())
print("Peso: ", funcionario.getPeso())
print("Altura: ", funcionario.getAltura())
print("Salario: ", funcionario.getSalario())

funcionario.setNome("Maria")
funcionario.setIdade(20)
funcionario.setFuncao("Analista de Sistemas")
funcionario.setNascimento("01/06/2002")
funcionario.setTelefone("987654321")
funcionario.setPeso(70)
funcionario.setAltura(1.80)
funcionario.setSalario(2100)

print("\nNome: ", funcionario.getNome())
print("Idade: ", funcionario.getIdade())
print("Função na empresa: ", funcionario.getFuncao())
print("Data de nascimento: ", funcionario.getNascimento())
print("Telefone: ", funcionario.getTelefone())
print("Peso: ", funcionario.getPeso())
print("Altura: ", funcionario.getAltura())
print("Salario: ", funcionario.getSalario())