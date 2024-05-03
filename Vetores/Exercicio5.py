numbers = [];
inputNumber = int(1);

print(f'Digite números para serem armazenados no vetor. Ao final, exibiremos os números em ordem crescente.');
print(f'Aperte ENTER para parar.');

while (True):
    try:
        inputNumber = int(input('Digite: '));
    
        numbers.append(inputNumber);
    except:
        break;


# Processamento

print(f'Vetor Não ordenado: {numbers}');

numbers.sort();

print(f'Vetor ordenado: {numbers}');    
