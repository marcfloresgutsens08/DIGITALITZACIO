nota = float(input("Introdueix una nota entre 0 i 10: "))

if nota < 5:
    print("Suspès")
elif nota < 7:
    print("Aprovat")
elif nota < 9:
    print("Notable")
else:
    print("Excel·lent")