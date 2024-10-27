# def fact(n):
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i
#     return factorial
#
#
# print(fact(5))

def fact(n):
    if n == 0:  # 0! = 1
        return 1
    return fact(n - 1) * n  # n! = (n - 1)! * n


print(fact(5))