class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def getNome(self):
        return self.nome
    
    def getPreco(self):
        return self.preco
    
    def getEstoque(self):
        return self.estoque
    
    def removerDoEstoque(self, qtd):
        if self.estoque >= qtd:
            self.estoque -= qtd
            return True
        return False

class Pedido:
    def __init__(self):
        self.produtos = []
    
    def calcularTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total
    
    def adicionarProduto(self, produto):
        self.produtos.append(produto)
    
    def listarProdutos(self):
        for p in self.produtos:
            print("Produto: %s - Preço: %s" % (p.getNome(), p.getPreco()))

class Mercado:
    def __init__(self):
        self.produtos = []
    
    def adicionarProduto(self, nome, preco, estoque):
        produto = Produto(nome, preco, estoque)
        self.produtos.append(produto)
    
    def listarProdutos(self):
        for produto in self.produtos:
            print(produto.getNome(), produto.getPreco(), produto.getEstoque())
    
    def adicionarAoPedido(self, produto, qtd, pedido):
        for p in self.produtos:
            if produto == p.getNome():
                if p.removerDoEstoque(qtd):
                    for i in range(qtd):
                        pedido.adicionarProduto(p)
                    return True
                return False

mercado = Mercado()
mercado.adicionarProduto("Celular", 1000, 10)
mercado.adicionarProduto("Notebook", 2000, 10)
mercado.adicionarProduto("Tablet", 500, 10)
mercado.adicionarProduto("Teclado", 100, 10)
mercado.adicionarProduto("Mouse", 50, 10)
mercado.adicionarProduto("Monitor", 500, 10)

pedido = Pedido()

print("\nProdutos disponíveis:")

mercado.listarProdutos()

print("\nadicionado 2 celulares ao pedido\n")

mercado.adicionarAoPedido("Celular", 2, pedido)
pedido.listarProdutos()

print("\nadicionar mais que o produto em estoque\n")
mercado.adicionarAoPedido("Celular", 9, pedido)

print("\nProdutos no pedido:")
pedido.listarProdutos()

print("\nadicionar 4 notebooks ao pedido\n")
mercado.adicionarAoPedido("Notebook", 3, pedido)

print("\nProdutos no pedido:")
pedido.listarProdutos()

print("\nTotal do pedido: %s" % pedido.calcularTotal())
