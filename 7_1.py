print("введите строку")
str = input()
is_polynome = True
str_len = len(str)
for i in range(str_len // 2):
    if str[i] != str[str_len - i - 1]:
        is_polynome = False
        break

if is_polynome:
    print("yes")
else:
    print("no")