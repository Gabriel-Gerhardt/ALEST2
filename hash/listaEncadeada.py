from nodo import Nodo

class listaEncadeada:
    def __init__(self,inicio =  None, fim= None, tamanho = 0):
        self.inicio = inicio
        self.fim =fim
        self.tamanho= tamanho



    def adicionar(self,chave):
        nodo = Nodo(chave)
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        else:
            assert self.fim is not None
            nodo.anterior = self.fim
            self.fim.proximo = nodo
            self.fim = nodo

    def buscar(self, chave):
        return self.buscarRecursivo(chave, self.inicio)


    def buscarRecursivo(self,chave,nodo):
        if nodo is None:
                return False
        if chave == nodo.valor:
            return True

        return self.buscarRecursivo(chave,nodo.proximo)


def main():
    lista = listaEncadeada()
    lista.adicionar(2)
    lista.adicionar(5)



main()
