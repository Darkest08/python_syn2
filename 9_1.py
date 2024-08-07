n = int(input())
data = list()
values = dict()


for i in range(n):
    data.append(int(input()))

for value in data:
    if not value in values.keys():
        values[value] = 1
    else:
        values[value] += 1
print(len(values.keys()))