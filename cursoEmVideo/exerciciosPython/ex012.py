quantidadeDeKM = float(input("Quantos KM o carro percorreu: "))
quantidadeDeDias = int(input("Quantos dias ele foi alugado: "))

# Em R$
precoPorDia = 60.00
precoPorKm = 0.15

resultado = (quantidadeDeKM * precoPorKm) + (quantidadeDeDias * precoPorDia)

print("O carro percoreu {}Km por {} dias; \nSabendo que por dia são R${:.2f} e por Km rodado são R${:.2f} \nO que resulta num total a pagar de R${:.2f}".format(quantidadeDeKM, quantidadeDeDias, precoPorDia, precoPorKm, resultado))
