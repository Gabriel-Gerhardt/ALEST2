class GrafoAdjecencia:

    def __init__(self, numVertices: int, direcionado: bool):
        self.numVertices = numVertices
        self.direcionado = direcionado
        self.listaAdjacencia = [[] for _ in range(numVertices)]


    def obterAdjacentes(self):
        return None




    def adicionarAresta(self, v, w):
        self.listaAdjacencia[v].append(w)
        if not(self.direcionado):
            self.listaAdjacencia[w].append(v);

            self.numArestas+=1;

    def removerAresta(self, v, w):
        self.listaAdjacencia[v].remove(w)
        if not(self.direcionado):
            self.listaAdjacencia[w].remove(v);

            self.numArestas-=1;

    def obterGrau(self, v):
        return len(self.listaAdjacencia[v])

    def adjacentes(self, v):
        return self.listaAdjacencia[v]

    def gerarDot(self):
        print("digraph G {" if self.direcionado else "graph G {")
        conectores = "->" if self.direcionado else "--"
        visitados = set()
        for v in range(self.numVertices):
            for w in self.listaAdjacencia[v]:
                if self.direcionado or (v, w) not in visitados and (w, v) not in visitados:
                    print(f"    {v} {conectores} {w};")
                    if not self.direcionado:
                        visitados.add((v, w))
        print("}")



def main():
    n = 5
    grafo = GrafoAdjecencia(n,True)

    grafo.adicionarAresta(0, 1)
    grafo.adicionarAresta(0, 2)
    grafo.adicionarAresta(1, 3)

    grafo.gerarDot()

main()
