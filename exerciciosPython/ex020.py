from random import shuffle

a1 = str(input("Digite o nome do aluno(a) N°1: "))
a2 = str(input("Digite o nome do aluno(a) N°2: "))
a3 = str(input("Digite o nome do aluno(a) N°3: "))
a4 = str(input("Digite o nome do aluno(a) N°4: "))

listaDeAlunos = [a1, a2, a3, a4]
shuffle(listaDeAlunos)

print("A ordem de apresentação será:", listaDeAlunos)
