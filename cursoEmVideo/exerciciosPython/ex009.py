entrada = float(input("Digite um valor: R$"));

# Volor do dollar de acordo com o vídeo 3/07/2017
# valorDoDollar = 3.27;

# Volor em 5/02/2022
valorDoDollar = 5.33
valorDoEuro = 6.10
valorDoRublo = 0.070

dollarConvertido = entrada / valorDoDollar
euroConvertido = entrada / valorDoEuro
rubloConvertido = entrada / valorDoRublo

print("Você possui ${:.2f} dolares com R${}.".format(dollarConvertido, entrada))
print("Você possui €{:.2f} euro com R${}.".format(euroConvertido, entrada))
print("Você possui ₽{:.2f} Rublo Russo com R${}.".format(rubloConvertido, entrada))