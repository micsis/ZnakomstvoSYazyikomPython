# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

X1, Y1 = map(float, input('Введите, через пробел, координаты первой точки: ').split(' '))
X2, Y2 = map(float, input('Введите, через пробел, координаты второй точки: ').split(' '))
R = round(((X2 - X1)**2 + (Y2 - Y1)**2)**(1 / 2), 3)
print(f'Засстояние между точками в 2D пространстве = {R}')