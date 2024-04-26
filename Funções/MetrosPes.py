metros = float(0);
result = float(0);

def metrosToPes(_metros:float):
    _result = float(0);

    _result = _metros * 3.28;

    return _result;

print("O algoritmo converterá o valor digitado em Metros para Pés.\n");

metros = float(input("Digite: "));

result = metrosToPes(metros);

print(f'Resultado: {result}');