# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = input('Введите трёхзначное число: ')


if len(x) == 3 and x.isdigit():
    v_1, v_2, v_3 = int(x[0]), int(x[1]), int(x[2])
    sum_value = v_1 + v_2 + v_3
    mult_value = v_1 * v_2 * v_3
    print(f'Сумма цифр числа = {sum_value}\nПроизведение цифр числа = {mult_value}')
else:
    print("Ошибка")

print(x)