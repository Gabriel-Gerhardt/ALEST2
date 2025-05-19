import random

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

# Exemplo: use listas PEQUENAS!
arr = [3, 2, 1,4,321]
sorted_arr, tries = bogo_sort(arr.copy())
print(f"Lista ordenada: {sorted_arr} em {tries} tentativas")
