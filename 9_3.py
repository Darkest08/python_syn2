row = list(map(int, input().split(' ')))
unique_values = set()

for val in row:
    if val in unique_values:
        print(f"{val} YES")
    else:
        print(f"{val} NO")
        unique_values.add(val)