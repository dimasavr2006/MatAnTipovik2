import numpy as np
import scipy
from matplotlib import pyplot as plt


def function(x):

    return 5 * np.sqrt(25 * x -88) - 3 + 32 * np.log(x) # Функция

phi = scipy.constants.golden # Константу брал из библиотеки
# phi = 0.5 * (1 + np.sqrt(5)) # Но можно и так считать, просто комментарии местами поменять

print("Введите интервал неопределённости (через пробел)")
a0, b0 = map(float, input().split())
print("Введите ε > 0 ")
epsilon = float(input())

counter = 0

if epsilon <= 0:
    raise ValueError("Точность ε должна быть положительным числом") # Ну тут вроде как всё должно быть понятно

extrValues = []
lengthsArray = []

while True:
    x1 = b0 - (b0 - a0) / phi # Считаем по формуле, для точек золотого сечения, брал из https://ru.wikipedia.org/wiki/Метод_золотого_сечения
    x2 = a0 + (b0 - a0) / phi # Считаем по формуле, для точек золотого сечения, брал из https://ru.wikipedia.org/wiki/Метод_золотого_сечения

    y1 = function(x1) # Подстановка значения x в функцию
    y2 = function(x2) # Подстановка значения x в функцию

    # Сохраняем значения для вывода данных на графике
    extrValues.append((x1, y1)) # Боковое значение
    lengthsArray.append(b0 - a0) # Длина отрезка

    if y1 >= y2: # Проверка того, в какую сторону мы смещаемся
        a0 = x1
    else:
        b0 = x2

    if abs(b0 - a0) < epsilon: # Условия завершения цикла
        x = (a0 + b0) / 2
        break

    counter += 1 # Счётчик количества итераций цикла

# Погрешность вводим как половину длины интервала
pogr = abs(b0 - a0) / 2


print("Точка: ", x) # Вывод в консоль
print("Значение функции в этой точке: ", function(x)) # Вывод в консоль
print("Количество повторений функции: ", counter) # Вывод в консоль (я на всякий это добавлю)
print("Погрешность: ", pogr) # Вывод в консоль

# График изменения положения точки экстремума
xCoord, yCoord = zip(*extrValues) # Тут распаковываем кортеж, чтобы получить координаты, сделано чтобы не писать много строк кода
plt.figure(figsize=(16, 9))
plt.plot(xCoord, yCoord, marker="o", linestyle="-", color="blue")
plt.title("Положение точки предполагаемого экстремума на каждой итерации")
plt.xlabel("X")
plt.ylabel("Значение функции")
plt.grid()
plt.show()

# График изменения длины промежутка неопределенности
plt.figure(figsize=(16, 9))
plt.plot(range(len(lengthsArray)), lengthsArray, marker="o", linestyle="-", color="red")
plt.title("Длина промежутка неопределенности с возрастанием числа итераций")
plt.xlabel("Итерация")
plt.ylabel("Длина промежутка")
plt.grid()
plt.show()