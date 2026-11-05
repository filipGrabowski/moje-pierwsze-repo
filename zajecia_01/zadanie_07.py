dni = 7
ask = int(input("Ile jest dni w tygodniu? (nie oszukuj)"))
if ask == dni:
    print("Gratulacje, użytkowniku!")
else:
    print("Ostatnia szansa: ")
    ask = int(input("Ile jest dni w tygodniu? (nie oszukuj)"))
    if ask == dni:
        print("Gratulacje, użytkowniku!")
    else:
        print("Jak możesz nie wiedzieć ile tydzień ma dni?")