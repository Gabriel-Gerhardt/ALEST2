package main

type heapmax struct {
	chaves []int
}

func (h *heapmax) inserir(chave int) {
	h.chaves = append(h.chaves, chave)
	h.swin(len(h.chaves) - 1)

}
func (h *heapmax) swin(posicao int) {
	pai := h.chaves[(posicao-1)/2]
	atual := h.chaves[posicao]

	if atual > pai {
		h.chaves[posicao-1/2] = atual
		h.chaves[posicao] = pai
		h.swin((posicao - 1) / 2)
	}

}

func (h *heapmax) heapify(posicao int) {
	pai := h.chaves[posicao]
	if (posicao*2 + 1) > len(h.chaves)-1 {
		return
	}
	filho1 := h.chaves[posicao*2+1]
	var filho2 int
	if posicao*2+2 <= len(h.chaves)-1 {
		filho2 = h.chaves[posicao*2+2]
	}

	if pai >= filho1 && (posicao*2+2 > len(h.chaves)-1 || pai >= filho2) {
		return
	}
	if filho1 > filho2 && pai < filho1 {
		h.chaves[posicao*2+1] = pai
		h.chaves[posicao] = filho1
		h.heapify(posicao*2 + 1)
	}
	if filho2 >= filho1 && pai < filho2 {
		h.chaves[posicao*2+2] = pai
		h.chaves[posicao] = filho2
		h.heapify(posicao*2 + 2)
	}

}

func (h *heapmax) removerMaximo() int {
	if len(h.chaves) == 0 {
		return 0
	}
	temp := h.chaves[len(h.chaves)-1]
	h.chaves[0] = temp
	newArray := h.chaves[:len(h.chaves)-1]
	h.chaves = newArray
	h.heapify(0)
	return temp

}
func (h *heapmax) heapsort() []int {

	// Primeiro, inserir todos no heap
	for _, valor := range h.chaves {
		h.inserir(valor)
	}

	// Agora, remover do heap para formar o array ordenado
	resultado := make([]int, len(h.chaves))
	for i := len(h.chaves) - 1; i >= 0; i-- {
		resultado[i] = h.removerMaximo()
	}

	return resultado
}
