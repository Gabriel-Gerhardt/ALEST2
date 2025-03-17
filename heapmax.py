class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        # Sobe o item até a posição correta
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            # Troca com o pai
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def _heapify_down(self, i):
        # Desce o item até a posição correta
        n = len(self.heap)
        while True:
            left = self._left_child(i)
            right = self._right_child(i)
            largest = i

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            # Troca com o maior filho
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def push(self, item):
        # Adiciona o item ao fim da lista e faz o heapify para manter a propriedade do heap
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove e retorna o maior item (que está na raiz)
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")

        # O maior item está na raiz
        max_item = self.heap[0]

        # Substituímos a raiz pela última folha e fazemos o heapify para manter a estrutura
        self.heap[0] = self.heap[-1]
        self.heap.pop() 
        self._heapify_down(0)

        return max_item

    def peek(self):
        # Retorna o maior item sem removê-lo
        if len(self.heap) > 0:
            return self.heap[0]
        raise IndexError("peek from empty heap")

    def __len__(self):
        return len(self.heap)


# Exemplo de uso
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(20)
max_heap.push(5)

print("Maior valor:", max_heap.peek())  # Maior valor será 20

# Removendo e mostrando os valores em ordem decrescente
while len(max_heap) > 0:
    print(max_heap.pop())  # Vai imprimir 20, 10, 5


