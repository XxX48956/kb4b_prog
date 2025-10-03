import random

strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]

preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]

obcane = 100

def procento_sumeni(jedna_preference):
    procento = 1 + (random.randint(-2,2) / 100) #na procenta
    nova_preference = round(jedna_preference * procento, 1)
    return nova_preference

def sumeni():
    nove_pole_preferenci = []
    celkem = 100
    for jedna_preference in preference:
        nova_preference = procento_sumeni(jedna_preference)
        nove_pole_preferenci.append(nova_preference)
        celkem -= nova_preference


    nove_pole_preferenci[-1] += round(celkem, 1) #doplneni zbytku do "jiné"
    nove_pole_preferenci[-1] = round(nove_pole_preferenci[-1], 5) #zaokrouhlení "jiné"


def checksum_nove_preference(nove_pole_preferenci):
    soucet = 0
    for i in nove_pole_preferenci:
        soucet += i
        print(round(soucet, 5))

sumeni()

def volebni_ucast():
    procento = 1 + random.randint(50, 80) /100
    ucast = round(obcane * procento)
    return ucast

print(volebni_ucast())