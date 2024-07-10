print("Введите вид питомца")
species = input()
print("Введите кличку питомца")
name = input()
print("Введите возраст питомца")
age = input()

age_ending = "лет"
if 0 < int(age) % 10 < 5:
    age_ending = "года" 

print(f"Это {species} по кличке \"{name}\", ему {age} {age_ending}.")