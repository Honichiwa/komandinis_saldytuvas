import os

os.system("cls")

produktai = {}

def produkto_tipas():
    print('-------[ Produkto tipas ]-------')
    print('1: Skystas produktas')
    print('2: Kietas produktas')
    print('3: Paruoštas produktas')
    produktas = input('Ivesti')

while True:
    os.system("cls")

    print("-------[ Šaldytuvas ]-------")
    print("1: Įdėti produktus")
    print("2: Išimti produktus")
    print("3: Peržiūrėti produktų sąrašą")
    print("4: Suskaičiuoti")
    print("0: Išeiti")

    pasirinkimas = input("Pasirinkite: ")

    if pasirinkimas > str(5) or pasirinkimas < str(0):  # neteisingas pasirinkimas
        while True:
            os.system("cls")
            print(
                "!!Neteisingas pasirinkimas, spauskite ENTER ir bandykite dar karta!!"
            )
            back = input("")
            break

    if pasirinkimas == "0":
        os.system("cls")
        print("-------[ bye bye ]-------")
        break

    if pasirinkimas == "1":  # pirmas pasirinkimas
        os.system("cls")
        
        while True:
            pasirinkimas_3 = input("ivevskite 0 gryzti i menu \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")
        while True:
            pasirinkimas_3 = input("ivevskite 0 gryzti i menu \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "3":  # trecias pasirinkimas
        os.system("cls")
        while True:
            pasirinkimas_3 = input("ivevskite 0 gryzti i menu \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "4":  # ketvirtasa pasirinkimas
        os.system("cls")
        while True:
            pasirinkimas_4 = input("ivevskite 0 gryzti i menu \n\u2794 ")
            if pasirinkimas_4 == "0":
                break
