row = list(map(int, input().split(' ')))
unique_values = dict()

for val in row:
    if val in unique_values.keys():
        print(f"{val} YES")
    else:
        print(f"{val} NO")
        unique_values[val] = 1