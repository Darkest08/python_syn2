def fact(val):
    ret = 1
    for i in range(1, val+1):
        ret *= i
    return ret

f1 = fact(int(input()))

rf = [fact(x) for x in range(f1, 0, -1)]

print(f1)
print(rf)