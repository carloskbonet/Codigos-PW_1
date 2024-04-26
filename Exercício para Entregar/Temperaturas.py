def celsiusToFahrenheit(tempCelsius : float):
    fahrenheit = float(0);

    fahrenheit = (tempCelsius * 1.8) + 32;

    print(f'Temperatura em °F: {fahrenheit}');
    return fahrenheit;


def fahrenheitToCelsius(tempFahr : float):
    celsius = float(0);

    celsius = (tempFahr - 32) / 1.8;

    print(f'Temperatura em °C: {celsius}');
    return celsius;