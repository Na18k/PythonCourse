catetoOposto = float(input("Qual é o valor do Cateto Oposto? "))
catetoAdjacente = float(input("Qual é o valor do Cateto Adjacente? "))

resultado = ((catetoOposto ** 2) + (catetoAdjacente ** 2)) ** (1/2)

print("O valor da Hipostenusa é: {:.2f}".format(resultado))