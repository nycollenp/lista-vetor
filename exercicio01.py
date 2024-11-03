def contar_negativos(valores):
    negativos = 0
    for i in range(len(valores)):
        if valores[i] < 0:
         negativos += 1
    return negativos


valores= [6, -5, -4, -7, -2]
print(contar_negativos(valores))