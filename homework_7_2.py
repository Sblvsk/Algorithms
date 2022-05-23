# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def qsort(arr, start=0, end=None):
    def subpart(arr, start, end, pivot_index):
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        pivot = arr[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if arr[y] <= pivot:
                arr[y], arr[x] = arr[x], arr[y]
                x += 1
            y += 1

        arr[start], arr[x - 1] = arr[x - 1], arr[start]
        return x - 1

    if end is None:
        end = len(arr) - 1
    if end - start < 1:
        return

    pivot_index = random.randint(start, end)
    x = subpart(arr, start, end, pivot_index)
    qsort(arr, start, x - 1)
    qsort(arr, x + 1, end)


ary = [random.randint(1, 50) for i in range(10)]
print(ary)
print(qsort(ary))
