# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# chr(97) из чисел в символы
# ord('a') из символов в числа
# 97-122 буквы в нижнем регистре
# 65-90 буквы в ВЕРХНЕМ регистре
# 32 - разница между верхнем и нижним регистром

request = int(input('Введите номер буквы Английского алфавита: '))
if request > 0 and request < 27:
    print(chr(96+request))
else:
    print("Ошибка")
