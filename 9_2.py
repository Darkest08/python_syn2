#вводите через пробел
list1 = list(map(int, input().split(' ')))
list2 = list(map(int, input().split(' ')))

values = set()
intersection_size = 0

for val in list1:
    values.add(val)

for val in values:
    if val in list2:
        intersection_size += 1

print(intersection_size)