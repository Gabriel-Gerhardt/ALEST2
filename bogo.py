import random

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    attempts = 1
    random.shuffle(arr)
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

# Exemplo: use listas PEQUENAS!
arr = [3, 2, 1,4,321]
bestVal =100000
i=0
while i<50:
    sorted_arr, tries = bogo_sort(arr.copy())
    if tries< bestVal:
        bestVal = tries

    print(f"Lista ordenada: {sorted_arr} em {tries} tentativas")
    i+=1
print(bestVal)
