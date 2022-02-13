temperaturaCelsius = float(input("Informe a temperatura °C: "))

fahrenheit = ((9 * temperaturaCelsius) / 5) + 32
kelvin = temperaturaCelsius + 273.15

print("A temperatura de {}°C (Celcius) coresponde {}°F (Fahrenheit) e {}K (Kelvin)".format(temperaturaCelsius, fahrenheit, kelvin))
