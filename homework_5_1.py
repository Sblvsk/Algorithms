#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

enterprises = {}
value = int(input("Введите количество предприятий: "))

for i in range(1, value + 1):
    enterprise = input("Введите название предприятия ")
    enterprises[enterprise] = 0
    for i in range(1, 5):
        profit = int(input(f"Введите прибль за {i}ый квартал "))
        enterprises[enterprise] += profit


s = 0
for i in enterprises:
    s += enterprises[i]

avrg = s / value

for i in enterprises:
    if enterprises[i] > avrg:
        print(f"Годовая выручка предприятия {i} выше средней")

for i in enterprises:
    if enterprises[i] < avrg:
        print(f"Годовая выручка предприятия {i} ниже средней")



