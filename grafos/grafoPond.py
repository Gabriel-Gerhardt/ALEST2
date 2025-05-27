from aresta import Aresta

class GrafoPond:

    def __init__(self, numVertices: int, numArestas=0):
        self.numVertices = numVertices
        self.numArestas = 0
        self.listaAdjacencia = [[] for _ in range(numVertices)]



    def obterAdjacentes(self):
        return None

    def adicionarAresta(self, v, w, peso):
        aresta = Aresta(v,w,peso)
        self.listaAdjacencia[v].append(w)
        self.listaAdjacencia[w].append(v)
        self.numArestas+=1

    def removerAresta(self, v, w):
        self.listaAdjacencia[v].remove(w)
        self.listaAdjacencia[w].remove(v)

        self.numArestas-=1

    def obterGrau(self, v):
        return len(self.listaAdjacencia[v])

    def adjacentes(self, v):
        return self.listaAdjacencia[v]

    def gerarDot(self):
        print("graph G {" )
        conectores = "--"
        visitados = set()
        for v in range(self.numVertices):
            for w in self.listaAdjacencia[v]:
                print(f"    {v} {conectores} {w};")
                visitados.add((v, w))
        print("}")



def main():
    n = 5
    grafo = GrafoPond(n)

    grafo.adicionarAresta(0, 1,60)
    grafo.adicionarAresta(0, 2,60)
    grafo.adicionarAresta(1, 3,30)

    grafo.gerarDot()

main()
