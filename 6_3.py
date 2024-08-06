print("Введите числа A и B через пробел")
a, b = map(int, input().split(' '))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')
print()
