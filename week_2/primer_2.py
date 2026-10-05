numbers = list(range(1, 8))          # [1, 2, 3, 4, 5, 6, 7]
max_value = numbers[0]               # берём первое число как начальное

for n in numbers:
    if n > max_value:
        max_value = n
    if n == 5:                       # демонстрация break
        break   