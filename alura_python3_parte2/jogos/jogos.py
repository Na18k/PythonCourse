import forca
import adivinhacao

def escolher_jogo():
	print("=-="*12)
	print("Bem-Vindo, escolha um jogo!")
	print("=-="*12)
	print("")
	print("(1) Forca // (2) Adivinhação")

	jogo_escolhido = int(input("==> "))

	if(jogo_escolhido == 1):
		print("Jogando Forca.")
		forca.jogar()

	elif(jogo_escolhido == 2):
		print("Jogando Adivinhação.")
		adivinhacao.jogar()

if(__name__ == "__main__"):
	escolher_jogo()