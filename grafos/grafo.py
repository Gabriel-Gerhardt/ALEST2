class Grafo:
    def __init__(self, matriz: list[list[bool]], nVertices: int, nArestas: int):
        self.matriz = matriz
        self.nVertices = nVertices
        self.nArestas = nArestas

    def adicionarAresta(self, v, w):
        if not self.matriz[v][w]:
            self.matriz[v][w] = True
            self.matriz[w][v] = True
            self.nArestas += 1

    def removerAresta(self, v, w):
        if self.matriz[v][w]:
            self.matriz[v][w] = False
            self.matriz[w][v] = False
            self.nArestas -= 1

    def obterGrau(self, v):
        return sum(self.matriz[v])

    def adjacentes(self, v):
        return [i for i in range(self.nVertices) if self.matriz[v][i]]

    def gerarDot(self):
        print("graph G {")
        for i in range(self.nVertices):
            for j in range(i + 1, self.nVertices):
                if self.matriz[i][j]:
                    print(f"    {i} -- {j};")
        print("}")

    def buscarProfundidade(self, chave):
        visitados = [False] * self.nVertices
        self.buscarProfundidadeRecursivo(chave, visitados)

    def buscarProfundidadeRecursivo(self, chave, visitados):
        if visitados[chave]:
            return
        visitados[chave] = True
        print(chave)
        for i in self.adjacentes(chave):
            self.buscarProfundidadeRecursivo(i, visitados)


def main():
    n = 5
    matriz = [[False for _ in range(n)] for _ in range(n)]
    grafo = Grafo(matriz, n, 0)

    grafo.adicionarAresta(0, 1)
    grafo.adicionarAresta(0, 2)
    grafo.adicionarAresta(1, 3)

    grafo.buscarProfundidade(0)
    grafo.gerarDot()

main()
