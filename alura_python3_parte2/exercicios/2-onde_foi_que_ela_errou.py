# Fernanda, colocando em prática o que aprendeu neste
# capítulo, escreveu o seguinte código para testar se
# realmente aprendeu a criar uma condição if em seu código:

# minha_idade = 26
# idade_namorado = 25
# if(minha_idade == idade_namorado)
#     print('temos idades iguais')
# else:
#     print('temos idades diferentes')

# O problema é que o código dela não funciona.
# Consegue enxergar onde está o problema? Para quem está
# começando com Python, pode ser bem sutil. Descobriu?
# Clique em Ver Opinião do Instrutor, que você verá a resposta do instrutor.

# RESPOSTA:

# O erro é bem simples, no final da condição tanto IF quanto ELSE
# NÃO possuem ":", o que não indica que há um bloco a baixo deles

# O código funcional ficaria assim:

minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')

else:
    print('temos idades diferentes')
