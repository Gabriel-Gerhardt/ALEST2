from aresta import Aresta

class GrafoPond:

    def __init__(self, numVertices: int):
        self.numVertices = numVertices
        self.numArestas = 0
        self.listaAdjacencia = [[] for _ in range(numVertices)]

    def adicionarAresta(self, v, w, peso):
        aresta = Aresta(v, w, peso)
        self.listaAdjacencia[v].append(aresta)
        self.listaAdjacencia[w].append(aresta)  # Grafo não direcionado
        self.numArestas += 1

    def removerAresta(self, v, w):
        def deve_remover(a):
            return (a.ponto1 == v and a.ponto2 == w) or (a.ponto1 == w and a.ponto2 == v)

        self.listaAdjacencia[v] = [a for a in self.listaAdjacencia[v] if not deve_remover(a)]
        self.listaAdjacencia[w] = [a for a in self.listaAdjacencia[w] if not deve_remover(a)]
        self.numArestas -= 1

    def obterGrau(self, v):
        return len(self.listaAdjacencia[v])

    def adjacentes(self, v):
        return [a.ponto2 if a.ponto1 == v else a.ponto1 for a in self.listaAdjacencia[v]]

    def obterAdjacentes(self):
        return self.listaAdjacencia

    def gerarDot(self):
        print("graph G {" )
        conectores = "--"
        visitados = set()
        for v in range(self.numVertices):
            for aresta in self.listaAdjacencia[v]:
                a, b = aresta.ponto1, aresta.ponto2
                if (a, b) not in visitados and (b, a) not in visitados:
                    print(f"    {a} {conectores} {b} [label={aresta.peso}];")
                    visitados.add((a, b))
        print("}")


def main():
    n = 5
    grafo = GrafoPond(n)

    grafo.adicionarAresta(0, 1, 60)
    grafo.adicionarAresta(0, 2, 60)
    grafo.adicionarAresta(1, 3, 30)

    grafo.gerarDot()

main()
