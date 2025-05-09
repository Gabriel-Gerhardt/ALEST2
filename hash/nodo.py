class Nodo:
    def __init__(self, chave, valor=0, proximo=None, anterior=None):
        self.chave = chave
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior
