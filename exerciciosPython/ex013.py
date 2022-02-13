from unittest import result


entrada = float(input("Digite o valor do seu salário: R$"));

porcentagem = 15
porcentagemDeAumento = entrada*15/100;

resultado = entrada + porcentagemDeAumento

print("Seu salário de R${:.2f} com um aumento de {}% tem o valor de R${:.2f}".format(entrada, porcentagem, resultado))