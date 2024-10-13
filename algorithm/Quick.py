def quick_sort(arr):
    if len(arr) <= 1: #Базовый случай - если массив пустой или содержит один элемент, то он отсортирован
        return arr
    else:
        pivot = arr[len(arr)//2] #Выбираем опорный элемент
        left = [x for x in arr if x < pivot] # Разделяем массив на три части: меньшие, равные и большие элементы
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(array)
print("Отсортированный массив:", sorted_array)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]

        left = [x for x in arr if len(pivot) > len(x) or (len(pivot) == len(x) and pivot > x)]
        middle = [x for x in arr if len(pivot) == len(x) and pivot == x]
        right = [x for x in arr if len(pivot) < len(x) or (len(pivot) == len(x) and pivot < x)]

        return quick_sort(left) + middle + quick_sort(right)

array = ["banana", "apple", "pear", "kiwi", "strawberry"]
quick_array = quick_sort(array)
print(quick_array)
