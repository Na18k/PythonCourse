print("=-="*12)
print("Bem vindo ao jogo de Adivinhação!")
print("=-="*12)

numero_secreto = 42
numero_de_tentativas = 3
tentativas = 1

while(tentativas <= numero_de_tentativas):
	print("Tentativa {} de {}".format(tentativas, numero_de_tentativas))

	chute = int(input("Digite um número: "))
	acertou_chute = chute == numero_secreto
	chute_de_numero_maior = chute > numero_secreto
	chute_de_numero_menor = chute < numero_secreto

	if(acertou_chute):
		print("Você acertou; o número secreto é: {}".format(numero_secreto))
		numero_de_tentativas = 0

	else:
		print("Você errou!")

		if(chute_de_numero_maior):
			print("Seu chute está acima do número secreto.")

		elif(chute_de_numero_menor):
			print("Seu chute está abaixo do número secreto.")
	
	tentativas = tentativas + 1

print("")
print("Fim do jogo! ")


# CÓDIGO DO INSTRUTOR INSTRUTOR:

# print("*********************************")
# print("Bem vindo ao jogo de Adivinhação!")
# print("*********************************")
# numero_secreto = 42
# total_de_tentativas = 3
# rodada = 1

# while (rodada <= total_de_tentativas):
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))

#     chute_str = input("Digite o seu número: ")
#     print("Você digitou " , chute_str)
#     chute = int(chute_str)

#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto

#     if(acertou):
#         print("Parabéns! Você acertou!")
#     else:
#         if(maior):
#             print("O seu chute foi maior do que o número secreto!")
#         elif(menor):
#             print("O seu chute foi menor do que o número secreto!")

#     rodada = rodada + 1

# print("Fim do jogo")