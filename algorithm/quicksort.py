#БЫСТРАЯ СОРТИРОВКА
def quicksort(array):
    if len(array) < 2: #базовый случай
        return array
    else:
        pivot = array[0] #Рекурсивный случай(опорный элемент)
        less = [i for i in array[1:] if i < pivot] #Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot] #Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1, 10, 3, 0]))
