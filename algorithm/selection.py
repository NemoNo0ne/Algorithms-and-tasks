def selection_sort(arr):
    for i in range(len(arr)): # Предполагаем, что текущий элемент - наименьший
        min_idx = i
        # Ищем наименьший элемент по длине
        for j in range(i + 1, len(arr)):
            if len(arr[j]) < len(arr[min_idx]):
                min_idx = j
        # Вместо обмена сдвигаем элементы вправо и вставляем минимальный элемент
        min_value = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = min_value
    return arr

words = ["apple", "banana", "kiwi", "cherry", "pear"]
sorted_array = selection_sort(words)
print("Отсортированный массив:", sorted_array)