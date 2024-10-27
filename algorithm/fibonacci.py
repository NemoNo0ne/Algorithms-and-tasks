from timeit import timeit
from functools import lru_cache
from sys import setrecursionlimit

# def fib(n):
#     f_1, f = 1, 1
#     for i in range(n - 1):
#         f_1, f = f, f_1 + f
#     return f
#
#
# print(f"Среднее время вычисления: "
#       f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 3)} с.")

# from timeit import timeit
# from sys import setrecursionlimit
#
#
# def fib(n):
#     if n not in cash:
#         cash[n] = fib(n - 1) + fib(n - 2)
#     return cash[n]
#
#
# setrecursionlimit(2000)
# cash = {0: 1, 1: 1}
# print(f"Среднее время вычисления: "
#       f"{round(timeit('fib(1000)', number=10, globals=globals()) / 10, 6)} с.")

@lru_cache(maxsize=1000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


print(f"Среднее время вычисления: "
      f"{round(timeit('fib(35)', number=10, globals=globals()) / 10, 6)} с.")

