import random

def create_matrix(x, y):
    m = list()
    for i in range(x):
        m.append(list())
        for j in range(y):
            m[i].append(random.randint(-10,10))
    return m

def add_matrix(m1, m2, x, y):
    m = create_matrix(x, y)
    for i in range(x):
        for j in range(y):
            m[i][j] = m1[i][j] + m2[i][j]
    return m

def print_matrix(m):
    for arr in m:
        for val in arr:
            print(val, end=" ")
        print()
    print("-----------------------------")
x = 5
y = 5
m1 = create_matrix(x, y)
m2 = create_matrix(x, y)
m3 = add_matrix(m1, m2, x, y)
print_matrix(m1)
print_matrix(m2)
print_matrix(m3)