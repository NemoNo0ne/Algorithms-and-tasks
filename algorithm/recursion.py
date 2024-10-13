def factorial(n):
    if n == 0:  # Базовый случай
        return 1
    else:
        return n * factorial(n - 1)  # Рекурсивный вызов

########################################################################################################################
#Поиск в структуре данных
#Используется для обхода данных в сложных структурах, таких как деревья. Например, для поиска значения в бинарном дереве.
########################################################################################################################
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    return search(node.left, target) or search(node.right, target)  # Рекурсивные вызовы

########################################################################################################################
#алгоритм быстрой сортировки
########################################################################################################################
def quicksort(arr):
    if len(arr) <= 1:  # Базовый случай
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)  # Рекурсивные вызовы



