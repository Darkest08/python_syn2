print("введите строку")
str = input()
output_str = ""
index = 0
space_row = False
for character in str:
    if character == ' ':
        if not space_row:
            output_str += character
        space_row = True
    else:
        output_str += character
        space_row = False
print(output_str)