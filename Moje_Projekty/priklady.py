import random

def random_priklad():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    vysledek = 0
    znamenko_index = random.randint(1,3)
    if znamenko_index == 1:
        print(f"{a} + {b} = ", end="")
        vysledek = a + b
    elif znamenko_index == 2:
        print(f"{a} - {b} = ", end="")
        vysledek = a - b
    elif znamenko_index == 3:
        print(f"{a} * {b} = ", end="")
        vysledek = a * b
    else:
        print("ERROR")
    
    vstup = int(input(""))
    return vstup == vysledek

score = 0
pocet_prikladu = int(input("Kolik chceš řešit příkladů? \n>:"))
for i in range(pocet_prikladu):
    if random_priklad():
        score += 1

print(f"Vyřešil jsi {score}/{pocet_prikladu}")