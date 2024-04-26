
numbers = [];
inputNumber = int(0);
higher = int(0);

print('O algoritmo exibe o maior valor digitado.\n');

# Inputs

while ( inputNumber != -1 ):
    print(f'Digite um número para continuar ou -1 para encerrar.');
    inputNumber = int(input('Digite: '));

    if (inputNumber == -1):
        break;
    else:
        numbers.append(inputNumber);


# Processamento

print(f'O vetor tem {len(numbers)} numeros');

higher = numbers[0];

print(numbers);

for i in range(0 , len(numbers)):
    if ( higher < numbers[i] ):
        print(f'{numbers[i]} é maior que {higher}, portanto vou guardar {numbers[i]}');
        higher = numbers[i];
        

print(f'O maior número é : {higher}');