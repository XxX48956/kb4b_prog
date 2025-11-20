path = "Moje_Projekty\output\chatlog.txt"

name = input("Zadej jméno: ")
exit = False
while not exit:
    msg = input("Zadej zprávu: ")
    if msg.lower() == "konec":
        break
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}: {msg}\n")
    