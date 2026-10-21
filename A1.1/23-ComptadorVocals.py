frase = "enginyeria"
vocals = 0

for lletra in frase:
    if lletra in "aeiou":
        vocals = vocals + 1

print(f"La frase té {vocals} vocals.")