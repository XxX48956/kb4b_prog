def delitele(n):
    for i in range(1, n+1):
        if not n % i:
            print(i)

#delitele(12)

def stairs(height, char):
    for i in range(1, height+1):
        print(char*i)

#stairs(5, "h")

def SSNumber(number):
    array = str(number).split("/")
    if not (len(array[0]) == 6 and len(array[1]) == 4):
        print("*Invalide soc. sec. number*")
        return
    birth = array[0]
    year = birth[0:2] 
    preYear = "19" if int(year) > 25 else "20" 
    month = birth[2:4]
    sex = "*Žena*" if int(month) > 12 else "*Muž*"
    day = birth[4:6]

    print(year, month, day, preYear, sex)

SSNumber("987654/3210")