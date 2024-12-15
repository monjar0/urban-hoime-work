#Объявите функцию get_matrix и напишите в ней параметры n, m и value.
#Создайте пустой список matrix внутри функции get_matrix.
#Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
#В первом цикле добавляйте пустой список в список matrix.
#Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
#Во втором цикле пополняйте ранее добавленный пустой список значениями value.
#После всех циклов верните значение переменной matrix.
#Выведите на экран(консоль) результат работы функции get_matrix.

#Объявите функцию get_matrix и напишите в ней параметры n, m и value.
def get_matrix(n, m, value):
    # Создайте пустой список matrix внутри функции get_matrix.
    matrix = []

    # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
    for _ in range(n):
        row = []
        for _ in range (m):
            row.append(value)
        matrix.append(row)
    return matrix
# Примеры вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата на экран
print(result1)
print(result2)
print(result3)
