import os

os.system("cls")

to_do = {}
done = []

while True:
    os.system("cls")

    print("-------[ Programa ]-------")
    print("1: Prideti uzduoti")
    print("2: Patikrinti visas uzduotis")
    print("3: Istrinti uzduoti")
    print("4: History")
    print("0: išeiti")

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
            print("Iveskite nauja uzduoti arba ivevskite 0 gryzti i menu")
            task = input("\u2794 ")
            if task == "0":
                os.system("cls")
                break
            else:
                os.system("cls")
                to_do[task] = "in progress"
                print(task + " - buvo pridetas prie -to do list-\n")

    if pasirinkimas == "2":  # antras pasirinkimas
        os.system("cls")
        while True:
            if list(to_do.keys()) != []:
                for indeksas, reiksme in enumerate(to_do):
                    indeksas += 1
                    print(indeksas, ".", reiksme, to_do[reiksme])
            else:
                print("nera sukurtu uzduociu")

            try:
                pasirinkimas_2_1 = int(
                    input(
                        "\nPasirinkite uzduoti arba ivevskite 0 gryzti i menu \n\u2794 "
                    )
                )
                os.system("cls")
                if pasirinkimas_2_1 != 0:
                    os.system("cls")
                    print(
                        f"{list(to_do.keys())[pasirinkimas_2_1 - 1]} {list(to_do.values())[pasirinkimas_2_1 - 1]}\n"
                    )
                    p_sk2 = int(
                        input(
                            "ar norite istrinti - 1 ar pakeisti uzduoties statusa? - 2\n\u2794 "
                        )
                    )
                    if p_sk2 == 1:
                        del to_do[list(to_do.keys())[pasirinkimas_2_1 - 1]]
                        os.system("cls")
                    if p_sk2 == 2:
                        p_sk3 = int(
                            input(
                                "pasirinkite uzduoties statusa - 1 done, 2 - in progress"
                            )
                        )

                        if p_sk3 == 1:
                            to_do[list(to_do.keys())[pasirinkimas_2_1 - 1]] = "done"

                        if p_sk3 == 2:
                            to_do[
                                list(to_do.keys())[pasirinkimas_2_1 - 1]
                            ] = "in progress"
            except (ValueError, IndexError) as error:
                os.system("cls")
                continue

            if pasirinkimas_2_1 == 0:
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
