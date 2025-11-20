import random


path = "Moje_Projekty\output\output.txt"

minimum_n = int(input("Zadej minimální hodnotu: "))
maximum_n = int(input("Zadej maximální hodnotu: "))
n = int(input("Zadej počet generovaných čísel: "))

with open(path, "w", encoding="utf-8") as file:
    for i in range(n):
        file.write(str(random.randint(minimum_n, maximum_n))+"\n")

