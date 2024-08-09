class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.gestor = None
        self.empregados = []
    
    def __str__(self):
        return "Nome: %s - Salario: %s" % (self.nome, self.salario)
    
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def setNome(self, nome):
        self.nome = nome
    
    def setSalario(self, salario):
        self.salario = salario
    
    def adicionarEmpregado(self, empregado):
        self.empregados.append(empregado)
    
    def getEmpregados(self):
        return self.empregados
    
    def setGestor(self, gestor):
        self.gestor = gestor
    
    def setEmpregados(self, empregados):
        self.empregados = empregados
    
    def getGestor(self):
        return self.gestor
    
    def buscarEmpregado(self, nome):
        for empregado in self.empregados:
            if empregado.getNome() == nome:
                return empregado
        return None
    
    def listarEmpregados(self):
        for empregado in self.empregados:
            print(empregado)

class Gestao:
    def __init__(self):
        self.funcionarios = []
        self.gestores = []
    
    def adicionarFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def adicionarGestor(self, gestor):
        self.gestores.append(gestor)
    
    def listarFuncionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)
    
    def listarGestores(self):
        for gestor in self.gestores:
            print(gestor)
    
    def cadastrarGestor(self, nome, salario):
        gestor = Funcionario(nome, salario)
        self.adicionarGestor(gestor)
    
    def cadastrarFuncionario(self, nome, salario):
        funcionario = Funcionario(nome, salario)
        self.adicionarFuncionario(funcionario)
    
    def buscarFuncionario(self, nome):
        for f in self.funcionarios:
            if f.getNome() == nome:
                return f
        return None
    
    def buscarGestor(self, nome):
        for g in self.gestores:
            if g.getNome() == nome:
                return g
        return None

gestao = Gestao()

joao = Funcionario("Joao", 1000)
gestao.adicionarFuncionario(joao)

print(gestao.buscarFuncionario("Joao"))

gestao.cadastrarGestor("Maria", 2000)

gestao.buscarFuncionario("Joao").setGestor(gestao.buscarGestor("Maria"))

print("\nGestor de Joao:")
busca = gestao.buscarFuncionario("Joao")
print(busca.getGestor())

gestao.cadastrarFuncionario("Jose", 500)
gestao.cadastrarGestor("Joana", 1000)

print("\nFuncionarios:")
gestao.listarFuncionarios()

print("\nGestores:")
gestao.listarGestores()