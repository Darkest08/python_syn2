print("Введите целое число")
val = int(input())

if val != 0:
    if val > 0:
        sign = "Положительное"
    else:
        sign = "Отрицательное"
    
    if val % 2 == 0:
        parity = "чётное"
    else:
        parity = "нечётное"
    print(f"{sign} {parity} число")
else:
    print("Нулевое число")
