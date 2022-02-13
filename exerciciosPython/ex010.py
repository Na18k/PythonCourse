altura = float(input("Digite a altura: "));
largura = float(input("Digite a largura: "));

area = altura * largura;
metroDeTinta = 2; # São necessários 2m² para usar um litro de tinta

resultado = area / metroDeTinta;

print("São necessarios {} litros para pintar {}m².".format(resultado, area))
