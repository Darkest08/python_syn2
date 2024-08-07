import collections


#скопировал с примера для простоты тестов
pets = {
    1:

        {

            "Мухтар": {

                "Вид питомца": "Собака",

                "Возраст питомца": 9,

                "Имя владельца": "Павел"

            },

        },

    2:

        {

            "Каа": {

                "Вид питомца": "желторотый питон",

                "Возраст питомца": 19,

                "Имя владельца": "Саша"

            },

        },
}

def get_id():
    print("Введите id питомца:")
    return int(input())

def check_id(id):
    if id in pets.keys():
        return True
    else:
        print("id вне БД")
        return False

def get_pet(id):
    print (pets[id])

def get_suffix(age):
    if age % 20 > 1 and age % 20 < 5:
        return (f"года")
    elif age % 20 == 1:
        return (f"год")
    else:
        return (f"лет")

def pets_list():
    for key, data in pets.items():
        print(f"{key} : {data}")

def create(id = -1):
    print("Введите через запятую информацию о питомце по образцу: кличка, вид, возраст, имя владельца")
    name, species, age, owner = input().split(', ')
    if id < 0:
        id = collections.deque(pets, maxlen=1)[0]
    pets[id+1] = {name : {
        "Вид питомца" : species,
        "Возраст питомца" : int(age),
        "Имя владельца" : owner,
    }}


def read(id):
    pet = pets[id].keys()[0]
    data = pets[id][pet]
    print(f"Это {data["Вид питомца"]} по кличке \"{pet}\". Возраст питомца: {data["Возраст питомца"]} {get_suffix(data["Возраст питомца"])}. Имя владельца: {data["Имя владельца"]}.")

def upadate(id):
        read(id)
        create(id)

def delete(id):
    pets.pop(id)

def menu():
    options = """
_МЕНЮ
Введите:
show - для вывода БД
show_by_id - для вывода информации питомце по id
add - для добавления питомца
update - для обновления информации о питомце
delete - для удаления информации о питомце
stop - для завершения программы
        """
    print(options)
    return input()

def handle_command(command):
    if command == "show":
        pets_list()
    elif command == "show_by_id":
        id = get_id()
        if check_id(id):
            get_pet(id)
    elif command == "add":
        create()
    elif command == "update":
        id = get_id()
        if check_id(id):
            create(id)
    elif command == "delete":
        id = get_id()
        if check_id(id):
            delete(id)
    elif command == "stop":
        return False
    else:
        print("Неизвестная комманда")
    print("Нажмите Enter для продолжения")
    input()
    return True

cont = True
while(cont):
    cont = handle_command(menu())