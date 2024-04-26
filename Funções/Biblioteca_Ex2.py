def celsiusToFahrenheit(tempCelsius : float):
    fahrenheit = float(0);

    fahrenheit = (tempCelsius * 1.8) + 32;

    print(f'Temperatura em °F: {fahrenheit}');
    return fahrenheit;


def metrosToPes(_metros:float):
    _result = float(0);

    _result = _metros * 3.28;

    print(f'Valor em Pés: {_result}')
    return _result;


def kmToMiles(_kms:float):
    _result = float(0);

    _result = _kms * 0.621371192;

    print(f'Valor em Milhas: {_result}')
    return _result;
