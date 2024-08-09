class Produto:
    def __init__(self, descricao, valor, codigo):
        self.descricao = descricao
        self.valor = valor
        self.codigo = codigo
    
    def __str__(self):
        return "Descricao: %s - Valor: %s - Codigo: %s" % (self.descricao, self.valor, self.codigo)
    
    def getDescricao(self):
        return self.descricao
    
    def getValor(self):
        return self.valor
    
    def getCodigo(self):
        return self.codigo
    
    def setDescricao(self, descricao):
        self.descricao = descricao
    
    def setValor(self, valor):
        self.valor = valor
    
    def setCodigo(self, codigo):
        self.codigo = codigo

class ProdutoPedido:
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd
    
    def __str__(self):
        return "Produto: %s - Qtd: %s" % (self.produto, self.qtd)
    
    def getProduto(self):
        return self.produto
    
    def getQtd(self):
        return self.qtd
    
    def setProduto(self, produto):
        self.produto = produto
    
    def setQtd(self, qtd):
        self.qtd = qtd

class Pedido:
    def __init__(self):
        self.pedidos = []
    
    def adicionarPedido(self, pedido):
        self.pedidos.append(pedido)
    
    def calcularTotal(self):
        total = 0
        for pedido in self.pedidos:
            total += pedido.getProduto().getValor() * pedido.getQtd()
        return total
    
    def listarPedidos(self):
        for pedido in self.pedidos:
            print("Produto: %s - Qtd: %s" % (pedido.getProduto().getDescricao(), pedido.getQtd()))
    
    def buscarPedido(self, codigo):
        for pedido in self.pedidos:
            if pedido.getProduto().getCodigo() == codigo:
                return pedido
        return None

banana = Produto("Banana", 2.5, 1)
uva = Produto("Uva", 3.5, 2)
maçã = Produto("Maçã", 4.5, 3)
laranja = Produto("Laranja", 5.5, 4)
bergamota = Produto("Bergamota", 6.5, 5)
morango = Produto("Morango", 7.5, 6)

frutas = [banana, uva, maçã, laranja, bergamota, morango]

pedido = Pedido()

i = 1
for fruta in frutas:
    pedido.adicionarPedido(ProdutoPedido(fruta, i))
    i += 1

pedido.listarPedidos()

print("\ntotal: %s" % pedido.calcularTotal())