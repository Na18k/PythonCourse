from math import radians, sin, cos, tan
angulo = float(input("Digite um angulo: "))

anguloRadiano = radians(angulo)
seno = sin(anguloRadiano)
cosseno = cos(anguloRadiano)
tangente = tan(anguloRadiano)

print("O SENO de {}° é igual à: {:.2f}".format(angulo, seno))
print("O COSSENO de {}° é igual à: {:.2f}".format(angulo, cosseno))
print("O TANGENTE de {}° é igual à: {:.2f}".format(angulo, tangente))
