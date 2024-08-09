class Livro:
    def __init__(self, nome, autor, ano):
        self.nome = nome
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return "Nome: %s - Autor: %s - Ano: %s" % (self.nome, self.autor, self.ano)
    
    def getNome(self):
        return self.nome
    
    def getAutor(self):
        return self.autor
    
    def getAno(self):
        return self.ano
    
    def setNome(self, nome):
        self.nome = nome
    
    def setAutor(self, autor):
        self.autor = autor
    
    def setAno(self, ano):
        self.ano = ano
    
    def adicionarLivro(self, livro):
        self.livros.append(livro)
    
    def devolverLivro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            return True
        return False

class Pessoa:
    def __init__(self, nome, idade, numero):
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.livros = []
    
    def __str__(self):
        return "Nome: %s - Idade: %s - Numero: %s" % (self.nome, self.idade, self.numero)
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def getNumero(self):
        return self.numero
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def setNumero(self, numero):
        self.numero = numero
    
    def adicionarLivro(self, livro):
        self.livros.append(livro)
    
    def devolverLivro(self, nomeLivro):
        for livro in self.livros:
            if livro.getNome() == nomeLivro:
                devolvido = livro
                self.livros.remove(livro)
                return devolvido
        return None
    
    def listarLivros(self):
        for livro in self.livros:
            print(livro)

class Emprestimo:
    def __init__(self):
        self.pessoas = []
        self.livros = []
    
    def cadastrarPessoa(self, nome, idade, numero):
        pessoa = Pessoa(nome, idade, numero)
        self.pessoas.append(pessoa)
    
    def cadastrarLivro(self, nome, autor, ano):
        livro = Livro(nome, autor, ano)
        self.livros.append(livro)
    
    def emprestarLivro(self, nomePessoa, nomeLivro):
        pessoa = self.buscarPessoa(nomePessoa)
        livro = self.buscarLivro(nomeLivro)
        if pessoa != None and livro != None:
            pessoa.adicionarLivro(livro)
            self.livros.remove(livro)
            return True
        return False
    
    def devolverLivro(self, livro):
        self.livros.append(livro)
    
    def listarLivros(self):
        for livro in self.livros:
            print(livro)
    
    def listarPessoas(self):
        for pessoa in self.pessoas:
            print(pessoa)

    def buscarPessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def buscarLivro(self, nome):
        for livro in self.livros:
            if livro.getNome() == nome:
                return livro
        return None

em = Emprestimo()

em.cadastrarLivro("As Aventuras de Pi", "Yann Martel", "2012")
em.cadastrarLivro("Os Miseráveis", "Victor Hugo", "2014")
em.cadastrarLivro("Diário de um Banana 16: Bola Fora", "Jeff Kinney", "2021")

em.listarLivros()

em.cadastrarPessoa("João", 20, "123456789")
em.cadastrarPessoa("Maria", 20, "987654321")
em.cadastrarPessoa("Pedro", 20, "123456789")

em.emprestarLivro("João", "As Aventuras de Pi")
em.emprestarLivro("Maria", "Os Miseráveis")

print("\n")
em.listarLivros()

print("\n")
livro = em.buscarPessoa("João").devolverLivro("Harry Potter")
if livro != None:
    em.devolverLivro(livro)

print("\n")
em.listarLivros()

em.emprestarLivro("Maria", "Harry Potter")

print("\n")
em.listarLivros()

print("\nlivros emprestados Maria:")
em.buscarPessoa("Maria").listarLivros()
print("\nlivros emprestados João:")
em.buscarPessoa("João").listarLivros()