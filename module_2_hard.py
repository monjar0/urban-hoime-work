def find_password(n):
    # Строка для результата
    result = ""

    # Перебираем все числа от 1 до n
    for a in range(1, n + 1):
        # Ищем b от 1 до n
        for b in range(1, n + 1):
            # Проверяем кратность суммы n
            if (a + b) % n == 0:
                # Если условие выполняется, добавляем пару к строке результата
                result += str(a) + str(b)

    # Возвращаем результат
    return result


# Пример вызова
n = int(input("Введите число от 3 до 20: "))
password = find_password(n)
print("Нужный пароль:", password)