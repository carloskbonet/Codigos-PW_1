def metrosToPes(_metros:float):
    _result = float(0);

    _result = _metros * 3.28;

    print(f'Valor em Pés: {_result}')
    return _result;

def PesToMetros(_pes:float):
    _result = float(0);

    _result = _pes / 3.28;

    print(f'Valor em Metros: {_result}')
    return _result;
