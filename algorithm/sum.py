def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])
arr = [2,4,6]
print(sum(arr))