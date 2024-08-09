class Pneu:
    def __init__(self, aro, psi):
        self.aro = aro
        self.psi = psi
    
    def __str__(self):
        return "Aro: %s - PSI: %s" % (self.aro, self.psi)
    
    def getAro(self):
        return self.aro
    
    def getPsi(self):
        return self.psi
    
    def setAro(self, aro):
        self.aro = aro
    
    def setPsi(self, psi):
        self.psi = psi

class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia
    
    def __str__(self):
        return "Cilindradas: %s\nPotencia (cv): %s" % (self.cilindrada, self.potencia)
    
    def getCilindrada(self):
        return self.cilindrada
    
    def getPotencia(self):
        return self.potencia
    
    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    
    def setPotencia(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.pneus = []
        self.motor = None
    
    def __str__(self):
        return "Marca: %s\nModelo: %s\nAno: %s" % (self.marca, self.modelo, self.ano)
    
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def getAno(self):
        return self.ano
    
    def getMotor(self):
        return self.motor
    
    def getPneus(self):
        return self.pneus
    
    def setMarca(self, marca):
        self.marca = marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def setAno(self, ano):
        self.ano = ano
    
    def setMotor(self, motor):
        self.motor = motor
    
    def addPneu(self, pneu):
        self.pneus.append(pneu)

fusca = Carro("Honda", "City", 2009)

for i in range(0, 4):
    fusca.addPneu(Pneu(15, 30))

fusca.setMotor(Motor(1496, 116))

print("\nInformações do carro\n")

print(fusca)
print("Motor: %s" % fusca.getMotor())
print("Pneus: %s" % fusca.getPneus()[0])