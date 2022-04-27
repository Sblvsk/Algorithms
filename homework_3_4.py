# 4. Определить, какое число в массиве встречается чаще всего.

import random

values = [random.randint(1, 10) for i in range(20)]
print(values)

result = [0] * 11
best = 0

for i in values:
    result[i] += 1
    if result[i] > result[best]:
        best = i

print(best)

