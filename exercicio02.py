def maior_elemento(inteiros):
    maior = inteiros[0]
    for i in range(len(inteiros)):
        if inteiros[i] > maior:
            maior = inteiros[i]
    return maior


inteiros = [1, 2, 3, 6, 50, 67, 41, 54, 8, 4,]
print(maior_elemento(inteiros))