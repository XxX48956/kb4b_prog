path = "2. prace_se_soubory\data\slova.txt"

with open(path, "r", encoding="utf-8") as file:

    text = file.read()
    rows = 0
    words = 0

    for line in text.split():
        rows += 1

    for word in text.split(" "):
        words += 1

    chars_arr = [char for char in text if char != '\n']

    print("Pocet radku souboru je", rows)
    print(f"Počet znaků je {len(chars_arr)}")
    print(f"Počet slow je {words}")