entrada = input("Digite algo: ")

print("")
print("O que foi digitado foi: {}".format(entrada))
print("Que é do tipo primitivo: ", type(entrada))

print('==== O que "{}" pode ser: ===='.format(entrada))
print('')
print(" É um número: ", entrada.isnumeric())

print('----------------------------------------')
print(" É uma letra do alfabeto: ", entrada.isalpha())

print('----------------------------------------')
print(" É um alphanumerico: ", entrada.isalnum())

print('----------------------------------------')
print(" É um número decimal: ", entrada.isdecimal())

print('----------------------------------------')
print(" É um digito: ", entrada.isdigit())

print('----------------------------------------')
print(" É formado por letras minusculas: ", entrada.islower())

print('----------------------------------------')
print(" É formado por letras maiusculas: ", entrada.isupper())

print('----------------------------------------')
print(" É possível executar print(): ", entrada.isprintable())

print('----------------------------------------')
print(" É um espaço em branco: ", entrada.isspace())

print('----------------------------------------')
print(" Está capitalizada: ", entrada.istitle())

