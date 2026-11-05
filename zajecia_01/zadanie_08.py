imie = str(input("Podaj imię: "))
part1 = int(input("Podaj wynik pierwszej części: "))
part2 = int(input("Podaj wynik drugiej części: "))
suma = part1 + part2
print ("student:", imie)
print ("suma:", suma)
if (suma >= 15) and (part1 >= 5) and (part2 >= 5):
    print("status: zaliczone")
else:
    print("status: niezaliczone")
