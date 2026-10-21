preu = float(input("Introdueix el preu del producte: "))

if preu > 100:
    preu = preu * 0.9

print(f"El preu final és {preu:.2f} €")