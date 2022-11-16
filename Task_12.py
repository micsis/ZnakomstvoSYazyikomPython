# Задайте список из Numb чисел последовательности $(1+\frac 1 Numb)^Numb$ и выведите на экран их сумму.
# Пример:
# - Для Numb = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

Numb = int(input("Введите любое число: "))
N = []
for i in range(1, Numb+1):
    print(i, sep=" ",end=" ")
    if(i < Numb):
        print("+", sep=" ", end=" ")
    N.append(i)
print("=", sum(N))