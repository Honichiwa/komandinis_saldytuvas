import os

os.system("cls")

produktai = {"Skystas": {}, "Kietas": {}, "Paruoštas": {}}


def produkto_tipas():
    print("-------[ Produkto tipas ]-------")
    print("1: Skystas produktas")
    print("2: Kietas produktas")
    print("3: Paruoštas")
    pasirinkimas = int(input("Įveskite pasirinkimą:"))

    if pasirinkimas == 1:

        produktas = input('Įveskite produktą: ')
        kiekis = int(input('Įveskite produkto kiekį litrais: '))
        produktai['Skystas'][produktas] = kiekis
    elif pasirinkimas == 2:
        produktas = input('Įveskite produktą: ')
        kiekis = input('Įveskite produkto kiekį kilogramais: ')
        produktai['Kietas'][produktas] = kiekis
    else:
        produktas = int(input('Įveskite produktą: '))
        kiekis = int(input('Įveskite produkto kiekį vienetais: '))
        produktai['Kietas'][produktas] = kiekis
        produktas = input("Įveskite produktą: ")
        kiekis = int(input("Įveskite produkto kiekį litrais: "))
        produktai["Skystas"][produktas] = kiekis
        print(produktai)
    elif pasirinkimas == 2:
        produktas = input("Įveskite produktą: ")
        kiekis = input("Įveskite produkto kiekį kilogramais: ")
        produktai["Kietas"][produktas] = kiekis
    else:
        produktas = str(input("Įveskite produktą: "))
        kiekis = int(input("Įveskite produkto kiekį vienetais: "))
        produktai["Kietas"][produktas] = kiekis


def perziureti_saldytuva():
    os.system("cls")

    if list(produktai.keys()) != []:
        for indeksas, reiksme in enumerate(produktai):
            indeksas += 1
            print(indeksas, ".", reiksme, produktai[reiksme])
    else:
        print("nera sukurtu uzduociu")


def saldytuvo_sudetis():
    visi_produktai = list(produktai["Skystas"].values)
    return visi_produktai


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
        produkto_tipas()
        
        while True:
            pasirinkimas_3 = input(" 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")


        print('-------[ Produkto išimimas iš šaldytuvo ]-------')
        perziureti_saldytuva()

        tipas = input('Įveskite išimamo produkto tipą: ')
        while True:
            isimamas_produktas = input('Įveskite kokį produktą norite išimti: ')
            if not isimamas_produktas in produktai[tipas]:
                print('Tokio produkto nėra')
            else:
                break
        
        isimamo_produkto_kiekis = float(input('Įveskite kiek produkto išimsite: '))
        galutinis_kiekis = float(produktai[tipas][isimamas_produktas]) - isimamo_produkto_kiekis
        produktai[tipas][isimamas_produktas] = galutinis_kiekis
        
        if galutinis_kiekis == 0:
            del produktai[tipas][isimamas_produktas]
        perziureti_saldytuva()

        while True:
            pasirinkimas_3 = input("Įveskite 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "3":  # trecias pasirinkimas
        perziureti_saldytuva()
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
