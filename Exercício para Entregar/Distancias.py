def kmToMiles(_kms:float):
    _result = float(0);

    _result = _kms * 0.621371192;

    print(f'Valor em Milhas: {_result}')
    return _result;


def milesToKm(_miles:float):
    _result = float(0);

    _result = _miles / 0.621371192;

    print(f'Valor em Km: {_result}')
    return _result;
