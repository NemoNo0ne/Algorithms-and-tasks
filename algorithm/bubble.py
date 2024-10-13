def bubble_sort(arr):
    n = len(arr)
    # Проходим по всему массиву
    for i in range(n):
        # Внутренний цикл для соседних элементов
        for j in range(0, n-i-1):
            #Если элемент больше следующего, то меняем их местами
            if arr[j] > arr[i+1]:
                arr[j], arr[i+1] = arr[i+1], arr[j]
    return arr

# Запрашиваем у пользователя ввод массива чисел
user_input = input("Введите числа через пробел: ")
array = list(map(int, user_input.split()))  # Преобразуем строку в список чисел

# Сортируем массив
sorted_array = bubble_sort(array)

# Выводим результат
print("Отсортированный массив:", sorted_array)
