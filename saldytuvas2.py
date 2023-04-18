import os

os.system("cls")

produktai = {}


def produkto_tipai():
    print("-------[ Produkto tipas ]-------")
    print("1: Skystas produktas")
    print("2: Kietas produktas")
    print("3: Paruoštas")
    pasirinkimas = int(input("Įveskite pasirinkimą:"))


def perziureti_saldytuva():
    os.system("cls")

    if list(produktai.keys()) != []:
        for indeksas, reiksme in enumerate(produktai):
            indeksas += 1
            print(indeksas, ".", reiksme, produktai[reiksme])
    else:
        print("Saldytuvas tuscias")


def saldytuvo_sudetis():
    produktai
    return


while True:
    os.system("cls")

    print("-------[ Šaldytuvas ]-------")
    print("1: Įdėti produktus")
    print("2: Išimti produktus")
    print("3: Suskaičiuoti")
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
        perziureti_saldytuva()
        produktas = input("\nIveskite produkta: ")  # ivedame produkto pavadinima
        produkto_kiekis = float(
            input("\nIveskite produkto kieki: ")
        )  # ivedame produkto kieki
        produktai[
            produktas
        ] = produkto_kiekis  # kiekvienas ivestas produktas sukuria zodyno nauja keys ir produkto kiekis sukuria to keys values

        while True:
            pasirinkimas_3 = input(" 0 grįžti į MENIU \n\u2794 ")
            if pasirinkimas_3 == "0":
                break

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")
        perziureti_saldytuva()
        while True:
       


            print("-------[ Produkto išimimas iš šaldytuvo ]-------")
            isimamas_produktas = input("Irasykite isimama produkta arba 0 grysti i MENIU: ")
            if isimamas_produktas == "0":
                break
            else:

                isimamas_kiekis = float(input("Isimamas kiekis: "))
                esamas_kiekis = produktai[isimamas_produktas]
                esamas_kiekis -=  isimamas_kiekis
                produktai[isimamas_produktas] = esamas_kiekis

                if esamas_kiekis <= 0:
                    del produktai[isimamas_produktas]




       
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
