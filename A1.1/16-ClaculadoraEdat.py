any_naixement = int(input("Introdueix el teu any de naixement: "))
any_actual = int(input("Introdueix l'any actual: "))

edat = any_actual - any_naixement

print(f"Tens {edat} anys.")

if edat >= 18:
    print("Ets major d'edat.")
else:
    print("Ets menor d'edat.")