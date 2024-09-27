class Carro:
    def carro(self,marca,modelo,ano,cor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor

carro=[]

def add_carro(marca, modelo, ano, cor):
    id = len(carro) + 1
    novos_carros = Carro(id, marca, modelo, ano, cor)
    carro.append(novos_carros)