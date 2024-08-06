print("Введите пятизначное число")
val = list(map(int, list(input())))
print(val[3] ** val[4] * val[2] / (val[0] - val[1]))