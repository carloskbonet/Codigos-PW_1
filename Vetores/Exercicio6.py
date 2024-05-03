numbers = [];
inputNumber = int(0);
check = int(0);
sum = int(0);

print('O algoritmo solicitará números. Aperte ENTER para parar.');

while (True):
    try:
        inputNumber = int(input('Digite: '));
    
        numbers.append(inputNumber);
    except:
        break;


for i in range(0 , len(numbers)):
    check = numbers[i] % 2;

    if (check == 0):
        sum = sum + numbers[i];

print(f'\nVetor: {numbers}');
print(f'A soma dos valores pares do vetor é: {sum}');