from grafoAdjecencia import GrafoAdjecencia



def main():
    grafo = GrafoAdjecencia(10,False)
    path = "10_arestas.txt"
    conteudo = open(path,"r")
    linha  = conteudo.readline()

    while(linha!=""):
        nomes = linha.split("--")
        print(nomes[0])
        print(nomes[1])
        grafo.adicionarAresta(nomes[0],nomes[1])
        linha = conteudo.readline()
main()
