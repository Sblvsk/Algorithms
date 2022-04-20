# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

x = int(input("Введите количество элементов прогрессии: "))

def progression(x):
    value = 1
    lst = []
    lst.append(value)
    for i in range(x):
        value = -(value/2)
        lst.append(value)
    return lst

print(progression(x))


def sum_progress(lst):
    x = 0
    for i in lst:
        x += i
    return x


print(sum_progress(progression(x)))