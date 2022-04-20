#2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


value = input("Введите число: ")

def counting(x):
    even = []
    not_even = []
    lst = []
    for i in x:
        lst.append(int(i))

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            not_even.append(i)
    return f"Четных - {len(even)}, нечетных - {len(not_even)}"

print(counting(value))


