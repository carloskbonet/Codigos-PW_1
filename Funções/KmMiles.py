kms = float(0);
result = float(0);

def kmToMiles(_kms:float):
    _result = float(0);

    _result = _kms * 0.621371192;

    return _result;

print("O algoritmo converterá o valor digitado em Km para Milhas.\n");

kms = float(input("Digite: "));

result = kmToMiles(kms);

print(f'Resultado: {round(result , 1)}');