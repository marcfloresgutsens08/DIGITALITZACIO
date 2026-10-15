text = "Hello World"
text2 = "Hola mon!!!"

iguals = 0

for i in range(len(text)):
    if text[i] == text2[i]:
        iguals += 1

print("Hi ha", iguals, "caràcters iguals en la mateixa posició")