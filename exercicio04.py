
def ordenar_numeros(inteiros):
    for i in range(len(inteiros)):
        for j in range(i+1, (len(inteiros))):
            if inteiros[j] < inteiros[i]:
                aux = inteiros[i]
                inteiros[i] = inteiros[j]
                inteiros[j] = aux
    return inteiros

inteiros = [1, 5, 4, 7, 6, 45,]
print(ordenar_numeros(inteiros))