# В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

values = [random.randint(1, 10) for i in range(10)]
print(values)

min_v = values[0]
max_v = values[0]

for i in range(len(values)):
    if values[i] > values[max_v]:
        max_v = i
    if values[i] < values[min_v]:
        min_v = i

print(values[min_v], values[max_v])

values[min_v], values[max_v] = values[max_v], values[min_v]
print(values)




