import random

def prin(argumento):
	print("\n"*argumento)

def placar(x, x2, y, z):
	print("="*4, "PLACAR", "="*4)
	print("/------------------------------|")
	print("|Tentativas Restantes:{:2}/{:2}".format(x, x2))
	print("|------------------------------")
	print("|Pontos Restantes:        {:2} ".format(y))
	print("|------------------------------")
	print("|Chutes: {}".format(z))
	print("|------------------------------|")



def jogar():
	print("=-="*12)
	print("Bem vindo ao jogo de Adivinhação!")
	print("=-="*12)
	prin(2)

	numero_secreto = random.randrange(1, 101)
	numero_de_tentativas = 3
	pontos = 100
	chutes = []
	pontos_perdidos = 0

	print("Escolha o nível de dificuldade.")
	print("(1) Fácil (2) Médio (3) Difícil")
	prin(1)
	nivel = int(input("==> "))

	if(nivel == 1):
		numero_de_tentativas = 20
	elif(nivel == 2):
		numero_de_tentativas = 10
	else:
		numero_de_tentativas = 5

	for tentativas in range(1,numero_de_tentativas + 1) :
		prin(1)
		print("Tentativa {} de {}".format(tentativas, numero_de_tentativas))
		chute = int(input("Digite um número entre 1 e 100: "))
		acertou_chute = chute == numero_secreto
		chute_de_numero_maior = chute > numero_secreto
		chute_de_numero_menor = chute < numero_secreto

		chutes.append(chute)

		if(chute < 1 or chute > 100):
			print("Você deve digitar um número entre 1 e 100!")
			continue

		if(acertou_chute):
			print("Você acertou; o número secreto é: {}".format(numero_secreto))
			placar(tentativas, numero_de_tentativas, pontos, chutes)
			break

		else:
			prin(1)
			print("Você errou!")

			if(chute_de_numero_maior):
				print("Seu chute está acima do número secreto.")

			elif(chute_de_numero_menor):
				print("Seu chute está abaixo do número secreto.")

			if(tentativas == numero_de_tentativas - 1):
				prin(1)
				print("O número secreto era: {}".format(numero_secreto))
				placar(0,numero_de_tentativas, pontos, chutes)


			pontos_perdidos = abs(pontos_perdidos - chute)
			pontos = pontos - pontos_perdidos

	print("")
	print("Fim do jogo! ")

if(__name__ == "__main__"):
	jogar()

# CÓDIGO DO INSTRUTOR:

# import random

# print("*********************************")
# print("Bem vindo ao jogo de Adivinhação!")
# print("*********************************")

# numero_secreto = random.randrange(1, 101)
# total_de_tentativas = 0
# pontos = 1000

# print("Qual o nível de dificuldade?")
# print("(1) Fácil (2) Médio (3) Difícil")

# nivel = int(input("Defina o nível: "))

# if(nivel == 1):
#     total_de_tentativas = 20
# elif(nivel == 2):
#     total_de_tentativas = 10
# else:
#     total_de_tentativas = 5

# for rodada in range(1, total_de_tentativas + 1):
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))

#     chute_str = input("Digite um número entre 1 e 100: ")
#     print("Você digitou ", chute_str)
#     chute = int(chute_str)

#     if(chute < 1 or chute > 100):
#         print("Você deve digitar um número entre 1 e 100!")
#         continue

#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto

#     if(acertou):
#         print("Você acertou e fez {} pontos!".format(pontos))
#         break
#     else:
#         pontos_perdidos = abs(numero_secreto - chute)
#         pontos = pontos - pontos_perdidos
#         if(maior):
#             print("O seu chute foi maior que o número secreto")
#             if (rodada == total_de_tentativas):
#                 print("O número secreto era {}. Você fez {}".format(
#                     numero_secreto, pontos))
#         elif(menor):
#             print("Você errou! O seu chute foi menor do que o número secreto.")
#             if (rodada == total_de_tentativas):
#                 print("O número secreto era {}. Você fez {}".format(
#                     numero_secreto, pontos))

# print("Fim do jogo")