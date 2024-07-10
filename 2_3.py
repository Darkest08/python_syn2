print("Введите минимальный размер инвестиций")
min_budget = int(input())
print("Введите бюджет Майкла")
m_budget = int(input())
print("Введите бюджет Ивана")
i_budget = int(input())

if m_budget + i_budget >= min_budget:
    if m_budget >= min_budget & i_budget >= min_budget:
        print(2)
    else:
        if m_budget >= min_budget:
            print("Mike")
        elif i_budget >= min_budget:
            print("Ivan")
        else:
            print(1)
else:
    print(0)