def encontrar_caracter(texto, letra):
    for i in range(len(texto)):
        if texto[i] == letra:
            return texto[:i+1]


texto = "nycolle"
letra = "o"
print(encontrar_caracter(texto, letra))
