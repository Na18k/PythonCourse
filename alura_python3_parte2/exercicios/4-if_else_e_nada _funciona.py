# Henrique, mesmo dando os primeiros passos com a
# linguagem Python, decidiu criar um sistema de
# identificação de usuários. É claro que em uma
# aplicação real é necessário acessar o banco de
# dados, entre outras coisas, mas usando o que
# ele já aprendeu, ele conseguiu algo parecido.
# Esse é o código do aluno:

# usuario = input("Informe o usuário do sistema!")

# if(usuario == "Flávio"):
#     print("Seja bem-vindo Flávio!")
# else(usuario == "Douglas"):
#     print("Seja bem-vindo Douglas!")
# else(usuario == "Nico"):
#     print("Seja bem-vindo Nico")
# else:
#     print("Usuário não identificado!")

# A ideia de Henrique é simples, porém não muito eficiente.
# Ele quer aceitar apenas os usuários Flávio, Douglas e Nico.
# No entanto, seu código não funciona!
# Consegue identificar a razão? Quebre a cabeça um pouquinho.

# --------------------------------------
# O erro de Henrique foi usar "else" e não "elif", pois
# else não recebe condição, o que faz com que o código
# não funcione corretamente.

# O código de forma coreta ficaria assim.

usuario = input("Informe o usuário do sistema! ")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
