import random


path = "2. prace_se_soubory\data\citaty.txt"
 
start_emoji_arr = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
end_emoji_arr = ["💥", "🔥", "❤️‍", "😎", "🤣"]
start_emoji = []

for i in range(random.randint(3, 5)):
    start_emoji = random.choices(start_emoji_arr, k=random.randint(3,5))

end_emoji = end_emoji_arr[random.randint(0, len(end_emoji_arr)-1)]

 
with open(path, "r", encoding="utf-8") as file:
    text = file.read()
    

    lines = []

    for line in text.split("\n"):
        lines.append(line)

    arr = [each.split(" - ") for each in lines]
    x = arr[random.randint(0, len(arr)-1)]
    
    
    [print(f"{each}", end=" ") for each in start_emoji]
    print()
    print(f"{x[0]}")
    print(f"### {x[-1]} ###")
    print(f"{end_emoji}")