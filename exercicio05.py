def somar_elementos(inteiros):
    soma = 0
    for i in range(len(inteiros)):
        soma += inteiros[i]
    return soma

inteiros = [5, 3, 2,]
print(somar_elementos(inteiros))