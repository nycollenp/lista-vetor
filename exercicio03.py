def menor_elemento(inteiros):
    menor = inteiros[0]
    for i in range(len(inteiros)):
        if inteiros[i] < menor:
            menor = inteiros[i]
    return menor


inteiros = [1, -5, 8, -7, 3]
print(menor_elemento(inteiros))