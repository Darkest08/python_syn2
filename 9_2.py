#вводите через пробел
list1 = list(map(int, input().split(' ')))
list2 = list(map(int, input().split(' ')))

values = dict()
intersection_size = 0

for val in list1:
    if not val in values.keys():
        values[val] = 1

for val in list2:
    if val in values.keys():
        intersection_size += 1

print(intersection_size)