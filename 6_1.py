print("Введите число вводимых чисел")
n = int(input())
amount_of_zeros = 0
print(f"Введите {n} целых чисел, скрипт вернёт число нулей")
for i in range(n):
    if int(input()) == 0:
        amount_of_zeros+=1
print(amount_of_zeros)