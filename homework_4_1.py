# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import time

numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(lst, find):
    left = 0
    right = len(lst)

    while left < right:
        mid = (right + left) // 2
        if lst[mid] == find:
            return mid
        if lst[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    return -1


start = time.time()
print(binary_search(numbs, 4))
print(time.time() - start)


def binary_search_rec(lst, find, left=0, right=None):
    if right is None:
        right = len(lst)
    if left > right:
        return -1

    mid = (right + left) // 2

    if find == lst[mid]:
        return mid
    if find < lst[mid]:
        return binary_search_rec(lst, find, left, mid - 1)
    else:
        return binary_search_rec(lst, find, mid + 1, right)


start = time.time()
print(binary_search_rec(numbs, 4))
print(time.time() - start)
