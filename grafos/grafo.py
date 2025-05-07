class Grafo:
    def __init__(self, matriz: list[list[bool]], nVertices: int, nArestas: int):
        self.matriz = matriz
        self.nVertices = nVertices
        self.nArestas = nArestas

    def adicionarAresta(self, v, w):
        if self.matriz[v][w] ==False:

            self.matriz[v][w] = True
            self.matriz[w][v] = True
            self.nArestas += 1

    def removerAresta(self,v,w):
        if self.matriz[v][w] ==True:

            self.matriz[v][w] = False
            self.matriz[w][v] = False
            self.nArestas -=1

    def obterGrau(self, v):
        cont=0
        for i in range(self.nVertices):
            if self.matriz[v][i] == True:
                cont+=1

        return cont


    def adjacentes(self,v):
        lista= []
        for i in range(self.nVertices):
            if self.matriz[v][i] == True:
                lista.append(i)

        return lista


    def gerarDot(self):
        print("graph G {")
        for i in range(self.nVertices):
            for j in range(i + 1, self.nVertices):
                if self.matriz[i][j]:
                    print(f"    {i} -- {j};")
        print("}")


def main():
    n = 5
    matriz = [[False for _ in range(n)] for _ in range(n)]
    grafo = Grafo(matriz, n, 0)

    grafo.adicionarAresta(0, 1)
    grafo.adicionarAresta(0, 2)
    grafo.adicionarAresta(1, 3)
    grafo.removerAresta(0,2)


    grafo.gerarDot()

main()
