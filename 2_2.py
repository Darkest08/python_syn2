vowels = {
    "a" : 0, 
    "e" : 0,
    "i" : 0, 
    "o" : 0,
    "u" : 0,
}

def counter(sign):
    if sign in vowels.keys():
        vowels[sign]+= 1

word = list(input())

for sign in word:
    counter(sign)

n_vovels = 0
for n in vowels.values():
    n_vovels+=n 

print(f"Число гласных {n_vovels} \nЧисло согласных {len(word) - n_vovels}")

for sign, amount in vowels.items():
    if amount == 0:
        print(f"{sign} : False")
    else:
        print(f"{sign} : {amount}")