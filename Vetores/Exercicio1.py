
numbers = [];
sum = int(0);
inputNumber = int(-1);

# Explicação
print('O algoritmo calculará a soma de todos os números inseridos.\n');

# Inputs
while(inputNumber != 0):
    print('Digite um número para inserir no vetor. Digite 0 para parar.');
    inputNumber = int(input('Digite: '));

    if (inputNumber == 0):
        break;
    else:
        numbers.append(inputNumber);


# Processamento

for i in range(0 , len(numbers)):
    sum = sum + numbers[i];

print(f'Números do vetor: {numbers}');
print(f'Somatória: {sum}');