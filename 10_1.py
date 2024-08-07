pets = dict()

def add_pet(pets, name, species, age, owner):
    pets[name] = {
        "Вид питомца" : species,
        "Возраст питомца" : int(age),
        "Имя владельца" : owner,
    }

def print_age(age):
    if age % 20 > 1 and age % 20 < 5:
        return (f"{age} года")
    elif age % 20 == 1:
        return (f"{age} год")
    else:
        return (f"{age} лет")

print("Введите через запятую информацию о питомце по образцу: кличка, вид, возраст, имя владельца")
data = input().split(', ')
add_pet(pets, data[0], data[1], data[2], data[3])

#по сути информация
for pet, data in pets.items():
    print(f"Это {data["Вид питомца"]} по кличке \"{pet}\". Возраст питомца: {print_age(data["Возраст питомца"])}. Имя владельца: {data["Имя владельца"]}.")