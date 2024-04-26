celsius = float(0);
result = float(0);

def celsiusToFahrenheit(tempCelsius : float):
    fahrenheit = float(0);

    fahrenheit = (tempCelsius * 1.8) + 32;

    return fahrenheit;

print("O algoritmo fará a conversão da temperatura digitada em °C para °F\n");

celsius = float(input("Digite: "));

result = celsiusToFahrenheit(celsius);

print(f'Resposta da função: {result}');
