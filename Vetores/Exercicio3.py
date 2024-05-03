numbers = [];
inputNumber = int(1);
sum = int(0);
media = float(0);

print('O algoritmo calculará a média dos números digitados.');

print('Digite números para serem inseridos no vetor. Aperte ENTER para parar.');

while (True):
    try:
        inputNumber = int(input('Digite: '));
    
        numbers.append(inputNumber);
    except:
        break;


# Processamento

print(f'\n{numbers}\n');

for i in range(0 , len(numbers)):
    sum = sum + numbers[i];
    print(f'Soma: {sum}  // Posição: {i}  // Vetor[i]: {numbers[i]}');


media = sum / len(numbers);

print(f'\nMédia obtida: {media}');
