class Produto:
    def __init__(self, preco, tamanho):
        self.preco = preco
        self.tamanho = tamanho
        self.vendido = False
    
    def __str__(self):
        return "Preço: %s - Tamanho: %s - Vendido: %s" % (self.preco, self.tamanho, self.vendido)
    
    def getPreco(self):
        return self.preco
    
    def getTamanho(self):
        return self.tamanho
    
    def isVendido(self):
        return self.vendido
    
    def setPreco(self, preco):
        self.preco = preco
    
    def setTamanho(self, tamanho):
        self.tamanho = tamanho
    
    def vender(self, vendido = True):
        self.vendido = vendido

class Vendedor:
    def __init__(self):
        self.comissao = 0
    
    def __str__(self):
        return "Comissão: %s" % self.comissao
    
    def getComissao(self):
        return self.comissao
    
    def setComissao(self, comissao):
        self.comissao = comissao
    
    def vender(self, produto):
        if produto.isVendido():
            return False
        produto.vender()
        self.comissao += produto.getPreco() * 0.1
        return True

class Comprador:
    def __init__(self,verba):
        self.verba = verba
    
    def __str__(self):
        return "Verba: %s" % self.verba
    
    def getVerba(self):
        return self.verba
    
    def setVerba(self, verba):
        self.verba = verba
    
    def comprar(self, produto):
        if self.verba >= produto.getPreco():
            self.verba -= produto.getPreco()
            return True
        return False

class Venda:
    def __init__(self, vendedor, comprador, produto):
        self.vendedor = vendedor
        self.comprador = comprador
        self.produto = produto
    
    def getVendedor(self):
        return self.vendedor
    
    def getComprador(self):
        return self.comprador
    
    def getProduto(self):
        return self.produto
    
    def setVendedor(self, vendedor):
        self.vendedor = vendedor
    
    def setComprador(self, comprador):
        self.comprador = comprador
    
    def setProduto(self, produto):
        self.produto = produto
    
    def concretizaVenda(self):
        if self.vendedor.vender(self.produto) and self.comprador.comprar(self.produto):
            self.produto.vender()
            return True
        return False
    
    def cancelaVenda(self):
        self.produto.vender(False)
        self.vendedor.setComissao(self.vendedor.getComissao() - self.produto.getPreco() * 0.1)
        self.comprador.setVerba(self.comprador.getVerba() + self.produto.getPreco())

prod = Produto(100, 10)

vendedor = Vendedor()

comprador = Comprador(1000)

venda = Venda(vendedor, comprador, prod)
venda.concretizaVenda()

print("\nvenda confirmada!\n")

print(venda.getVendedor())
print(venda.getComprador())
print(venda.getProduto())

venda.cancelaVenda()

print("\nvenda cancelada!\n")

print(venda.getVendedor())
print(venda.getComprador())
print(venda.getProduto())