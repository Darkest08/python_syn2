print("Введите натуральное число, скрипт вернёт число натуральных делителей данного числа")
x = int(input())
n_dividers = 1
divider = 1
while(divider <= x):
    divider+=1
    if x % divider == 0:
        n_dividers+=1

print(n_dividers)